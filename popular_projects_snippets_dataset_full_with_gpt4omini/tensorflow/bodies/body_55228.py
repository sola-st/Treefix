# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Returns a `FuncGraph` generated from `python_func`.

  Args:
    name: an identifier for the function.
    python_func: the Python function to trace.
    args: the positional args with which the Python function should be called;
      ignored if a signature is provided.
    kwargs: the keyword args with which the Python function should be called;
      ignored if a signature is provided.
    signature: a possibly nested sequence of `TensorSpecs` specifying the shapes
      and dtypes of the arguments. When a signature is provided, `args` and
      `kwargs` are ignored, and `python_func` is traced with Tensors conforming
      to `signature`. If `None`, the shapes and dtypes are inferred from the
      inputs.
    func_graph: Optional. An instance of FuncGraph. If provided, we will use
      this graph else a new one is built and returned.
    autograph: whether to use autograph to compile `python_func`.
      See https://www.tensorflow.org/guide/autograph for more information.
    autograph_options: additional knobs to control when `autograph=True`.
      See https://www.tensorflow.org/guide/autograph for more information.
    add_control_dependencies: If True, automatically adds control dependencies
      to ensure program order matches execution order and stateful ops always
      execute.
    arg_names: Optional list of argument names, used to give input placeholders
      recognizable names.
    op_return_value: Optional. A Tensor. If set and `python_func` returns
      Operations, those return values will be replaced with this value. If not
      set, returning an Operation triggers an error.
    collections: a dictionary of collections this FuncGraph should start with.
      If not specified (None), the FuncGraph will read (but not write to) the
      outer graph's collections that are not allowlisted, and both read and
      write to the outer graph's collections that are allowlisted. The current
      allowlisted collections are the global variables, the local variables, and
      the trainable variables. Defaults to None.
    capture_by_value: An optional boolean. If True, the func graph will capture
      Variables by value instead of reference. By default inherit from outer
      graphs, and failing that will default to False.
    create_placeholders: An optional boolean. If True, then func graph will
      create placeholders for the inputs as graph ops. If False, the input args
      and kwargs will be treated as the input placeholders.
    acd_record_initial_resource_uses: If `True` and `add_control_dependencies`
      is enabled, the results (those marked with
      AutomaticControlDependencies.mark_result) will be annotated with a private
      attribute, "_res_first_used_by", which points to the first nodes which
      used the any of the resources that the result op is using.

  Returns:
    A FuncGraph.

  Raises:
    TypeError: If any of `python_func`'s return values is neither `None`, a
      `Tensor` or a `tf.experimental.ExtensionType`.
  """
if op_return_value is not None:
    assert isinstance(op_return_value, ops.Tensor), op_return_value
if func_graph is None:
    func_graph = FuncGraph(
        name, collections=collections, capture_by_value=capture_by_value)
assert isinstance(func_graph, FuncGraph)
if add_control_dependencies:
    deps_control_manager = auto_control_deps.AutomaticControlDependencies(
        record_initial_resource_uses=acd_record_initial_resource_uses)
else:
    deps_control_manager = ops.NullContextmanager()

with func_graph.as_default(), deps_control_manager as deps_ctx:
    current_scope = variable_scope.get_variable_scope()
    default_use_resource = current_scope.use_resource
    current_scope.set_use_resource(True)

    if signature is not None:
        args = signature
        kwargs = {}

    if create_placeholders:
        func_args, func_kwargs = _create_placeholders(args, kwargs, arg_names)
    else:
        func_args, func_kwargs = args, kwargs

    input_trace_types = trace_type.from_value([func_args, func_kwargs])
    func_graph.inputs = input_trace_types._to_tensors([func_args, func_kwargs])  # pylint: disable=protected-access
    for arg in func_graph.inputs:
        if arg.dtype == dtypes.resource:
            func_graph._resource_tensor_inputs.add(arg)  # pylint:disable=protected-access

    signature_context = trace_type.InternalTracingContext()
    # Convert all Tensors into TensorSpecs before saving the structured inputs.
    # If storing pure concrete functions that are not called through polymorphic
    # functions, we don't have access to FunctionSpec, so we need to call the
    # TensorSpecs by their `arg_names` for later binding.
    func_graph.structured_input_signature = (
        convert_structure_to_signature(
            func_args, arg_names, signature_context=signature_context),
        convert_structure_to_signature(
            func_kwargs, signature_context=signature_context))

    # Note: `nest.flatten` sorts by keys, as does `_deterministic_dict_values`.
    # Variables to help check whether mutation happens in calling the function
    # Copy the recursive list, tuple and map structure, but not base objects
    func_args_before = nest.pack_sequence_as(
        func_args,
        nest.flatten(func_args, expand_composites=True),
        expand_composites=True)
    func_kwargs_before = nest.pack_sequence_as(
        func_kwargs,
        nest.flatten(func_kwargs, expand_composites=True),
        expand_composites=True)

    def convert(x):
        """Converts a function output to a Tensor."""
        if x is None:
            exit(None)
        if op_return_value is not None and isinstance(x, ops.Operation):
            # TODO(b/79881896): we currently can't capture external control deps, so
            # this won't work if x needs to be captured (i.e. if python_func returns
            # captured Operations).
            with ops.control_dependencies([x]):
                x = array_ops.identity(op_return_value)
        elif not isinstance(x, tensor_array_ops.TensorArray):
            try:
                x = ops.convert_to_tensor_or_composite(x)
            except (ValueError, TypeError):
                raise TypeError(
                    "To be compatible with tf.function, Python functions "
                    "must return zero or more Tensors or ExtensionTypes or None "
                    f"values; in compilation of {str(python_func)}, found return "
                    f"value of type {type(x).__name__}, which is not a Tensor or "
                    "ExtensionType.")
        if add_control_dependencies:
            x = deps_ctx.mark_as_return(x)
        exit(x)

    try:
        if autograph:
            from tensorflow.python import autograph  # pylint: disable=g-import-not-at-top
            _, original_func = tf_decorator.unwrap(python_func)

            def autograph_handler(*args, **kwargs):
                """Calls a converted version of original_func."""
                # TODO(mdan): Push this block higher in tf.function's call stack.
                try:
                    exit(autograph.converted_call(
                        original_func,
                        args,
                        kwargs,
                        options=autograph.ConversionOptions(
                            recursive=True,
                            optional_features=autograph_options,
                            user_requested=True,
                        )))
                except Exception as e:  # pylint:disable=broad-except
                    if hasattr(e, "ag_error_metadata"):
                        raise e.ag_error_metadata.to_exception(e)
                    else:
                        raise

        # Wrapping around a decorator allows checks like tf_inspect.getargspec
        # to be accurate.
            converted_func = tf_decorator.make_decorator(original_func,
                                                         autograph_handler)
            python_func = tf_decorator.rewrap(python_func, original_func,
                                              converted_func)

        else:
            _, original_func = tf_decorator.unwrap(python_func)

        func_outputs = python_func(*func_args, **func_kwargs)

        # invariant: `func_outputs` contains only Tensors, CompositeTensors,
        # TensorArrays and `None`s.
        func_outputs = variable_utils.convert_variables_to_tensors(func_outputs)
        func_outputs = nest.map_structure(
            convert, func_outputs, expand_composites=True)

        # flatten and unflatten func_args and func_kwargs to maintain parity
        # from flattening which sorts by key
        func_args = nest.pack_sequence_as(
            func_args,
            nest.flatten(func_args, expand_composites=True),
            expand_composites=True)
        func_kwargs = nest.pack_sequence_as(
            func_kwargs,
            nest.flatten(func_kwargs, expand_composites=True),
            expand_composites=True)
        check_func_mutation(func_args_before, func_kwargs_before, func_args,
                            func_kwargs, original_func)
    finally:
        current_scope.set_use_resource(default_use_resource)

    # Variables in `func_args`, `func_kwargs` should be explicit inputs
    # to the function, not captured inputs.
    graph_variables = list(func_graph._watched_variables)  # pylint: disable=protected-access
    arg_variables = object_identity.ObjectIdentitySet()
    inputs = []
    for arg in composite_tensor_utils.flatten_with_variables([func_args,
                                                              func_kwargs]):
        if isinstance(arg, resource_variable_ops.BaseResourceVariable):
            # Even if an argument variable was not used in the function, we've
            # already manually captured the resource Tensor when creating argument
            # placeholders.
            resource_placeholder = func_graph.pop_capture(arg.handle)
            if resource_placeholder is None:
                continue
            arg_variables.add(arg)
            inputs.append(resource_placeholder)
        elif isinstance(arg, ops.Tensor):
            inputs.append(arg)
    variables = [v for v in graph_variables if v not in arg_variables]
    func_graph.inputs = (
        inputs + func_graph.internal_captures + nest.flatten(
            func_graph.deferred_internal_captures, expand_composites=True))
    func_graph.structured_outputs = func_outputs
    # Returning a closed-over tensor does not trigger convert_to_tensor.
    func_graph.outputs.extend(
        func_graph.capture(x)
        for x in flatten(func_graph.structured_outputs)
        if x is not None)

    func_graph.variables = variables

if add_control_dependencies:
    func_graph.control_outputs.extend(deps_control_manager.ops_which_must_run)
    func_graph.collective_manager_ids_used = (
        deps_control_manager.collective_manager_ids_used)

exit(func_graph)
