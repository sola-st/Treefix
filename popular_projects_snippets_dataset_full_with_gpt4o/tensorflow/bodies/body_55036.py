# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""This is not what you want, see _create_definition_if_needed."""
if self._definition is not None or self._c_func is not None:
    exit()

# Copy variable collections (by reference) from the parent graph such that
# name based variable sharing (e.g. via tf.make_template) works between the
# func graph and parent graph.
variable_keys = []
variable_keys.extend(ops.GraphKeys._VARIABLE_COLLECTIONS)  # pylint: disable=protected-access
variable_keys.append(vs._VARSTORE_KEY)  # pylint: disable=protected-access

parent_graph = ops.get_default_graph()
collections_ref = {
    key: parent_graph.get_collection_ref(key) for key in variable_keys}

temp_graph = func_graph_from_py_func(
    self._func,
    self._arg_names,
    self._arg_types,
    self._func_name,
    self._capture_by_value,
    self._caller_device,
    collections_ref=collections_ref,
    allowlisted_stateful_ops=self._allowlisted_stateful_ops,
    capture_resource_var_by_value=self._capture_resource_var_by_value)

self._extra_inputs = temp_graph.extra_inputs
# pylint: disable=protected-access
self._sub_functions = temp_graph._functions
# pylint: enable=protected-access

# Extra kwargs are treated as attrs on the function def.
if self._func_name:
    base_func_name = self._func_name
else:
    base_func_name = function_utils.get_func_name(self._func)
    if self._grad_func:
        base_func_name += ("_%s" % self._grad_func.name)
kwargs_attr = _parse_kwargs_as_attrs(base_func_name, **self._extra_kwargs)

# FIXME(feyu): C API is always enabled now. The if-true branch never runs.
if not temp_graph._c_graph:  # pylint: disable=protected-access
    # Build the FunctionDef
    self._definition = graph_to_function_def.graph_to_function_def(
        temp_graph,
        temp_graph.get_operations(),
        temp_graph.inputs,
        temp_graph.outputs,
        out_names=self._out_names)

    for k in kwargs_attr:
        self._definition.attr[k].CopyFrom(kwargs_attr[k])

    # Hash the definition and its dependencies.
    self._hash_str = self._create_hash_str(
        self._definition.signature.input_arg,
        self._definition.signature.output_arg, self._definition.node_def)

    # Finally, we decide the function name to use.  If not specified,
    # make up something which is almost certainly unique (but deterministic).
    if not self._func_name:
        self._func_name = "_".join([base_func_name, self._hash_str])
    self._definition.signature.name = self._func_name
    if self._func.__doc__:
        self._definition.signature.description = self._func.__doc__

    self._op_def = self._definition.signature
else:  # C API is enabled
    output_names = ([compat.as_bytes(x) for x in self._out_names]
                    if self._out_names else [])
    description = self._func.__doc__ or None
    # pylint: disable=protected-access
    with temp_graph._c_graph.get() as c_graph:
        c_func = c_api.TF_GraphToFunction_wrapper(
            c_graph,
            base_func_name,
            self._func_name is None,  # append_hash_to_fn_name
            None,  # opers
            [t._as_tf_output() for t in temp_graph.inputs],
            [t._as_tf_output() for t in temp_graph.outputs],
            output_names,
            [],  # control_outputs
            [],  # control_output_names
            None,  # opts
            description)
    self._c_func = c_api_util.ScopedTFFunction(c_func, base_func_name)
    # pylint: enable=protected-access
    self._set_c_attrs(kwargs_attr)

    # Set cached fields: _op_def and _func_name (if not already set)
    self._op_def = self.definition.signature
    if self._func_name:
        assert self._func_name == self._op_def.name
    else:
        self._func_name = compat.as_str(self._op_def.name)

self._stateful_ops = [(op.name, op.type)
                      for op in temp_graph.get_operations()
                      if op._is_stateful]  # pylint: disable=protected-access
