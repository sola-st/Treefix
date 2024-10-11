# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Load a set of functions as concrete functions without captured inputs.

  Functions names are manipulated during load such that they do not overlap
  with previously created ones.

  Gradients are re-registered under new names. Ops that reference the gradients
  are updated to reflect the new registered names.

  Args:
    library: FunctionDefLibrary proto message.
    saved_object_graph: SavedObjectGraph proto message. If not passed in,
      concrete function structured signatures and outputs will not be set.
    load_shared_name_suffix: If specified, used to uniquify shared names.
      Otherwise, a unique name is generated.
    wrapper_function: An object that will be wrapped on newly created functions.

  Returns:
    Map of original function names in the library to instances of
    `ConcreteFunction` without captured inputs.

  Raises:
    ValueError: if functions dependencies have a cycle.
  """
library_function_names = set(fdef.signature.name for fdef in library.function)
functions = {}
renamed_functions = {}

# Our graph building code currently requires functions to be registered with
# some tf.Graph in order to import functions using the
# op-name-is-function-name calling convention. To avoid leaking memory into
# the global default graph when executing eagerly, we create a temporary
# Graph.
#
# TODO(b/205023033): Make this Graph creation unnecessary when executing
# eagerly by fixing function_def_to_graph_def.
if ops.executing_eagerly_outside_functions():
    graph = ops.Graph()
else:
    graph = ops.get_default_graph()

if load_shared_name_suffix is None:
    load_shared_name_suffix = "_load_{}".format(ops.uid())

# Custom gradient functions must be re-registered under new UIDs.
library_gradient_names = {}  # Maps old op type to old function name
new_gradient_op_types = {}  # Maps old gradient op type to new op type.
gradients_to_register = {}  # Maps old function name to new op type
for gdef in library.registered_gradients:
    if gdef.registered_op_type:
        new_op_type = custom_gradient.generate_name()
        old_op_type = compat.as_bytes(gdef.registered_op_type)

        library_gradient_names[old_op_type] = gdef.gradient_func
        new_gradient_op_types[old_op_type] = new_op_type
        gradients_to_register[gdef.gradient_func] = new_op_type

function_deps = {}
for fdef in library.function:
    function_deps[fdef.signature.name] = _list_function_deps(
        fdef, library_function_names, library_gradient_names)

loaded_gradients = {}
for fdef in _sort_function_defs(library, function_deps):
    orig_name = _fix_fdef_in_place(fdef, functions, load_shared_name_suffix,
                                   new_gradient_op_types)

    # Setup function signatures and outputs
    #
    # When concrete functions are created normally (i.e. when they're originally
    # created and not loaded via saved model), the inputs and outputs are
    # calculated based on the values passed in by the user and returned from the
    # original function, respectively. We don't have access to those anymore at
    # restore time, so we must instead pass them to the FuncGraph explicitly.
    structured_input_signature = None
    structured_outputs = None
    if (saved_object_graph is not None and
        orig_name in saved_object_graph.concrete_functions):
        # TODO(b/204324043): Offload the deserialization of the protos to the
        # first class objects by passing the actual protos. This is blocked on
        # importing `nested_structure_coder` in function.py causing a circular
        # dependency.
        proto = saved_object_graph.concrete_functions[orig_name]
        structured_input_signature = nested_structure_coder.decode_proto(
            proto.canonicalized_input_signature)
        structured_outputs = nested_structure_coder.decode_proto(
            proto.output_signature)

    # There is no need to copy all functions into the function def graph. It
    # leads to a O(n^2) increase of memory when importing functions and the
    # extra function definitions are a no-op since they already imported as a
    # function before and passed in explicitly (due to the topologic sort
    # import).
    with graph.as_default():
        func_graph = function_def_lib.function_def_to_graph(
            fdef,
            structured_input_signature=structured_input_signature,
            structured_outputs=structured_outputs)
    # Restores gradients for function-call ops (not the same as ops that use
    # custom gradients)
    _restore_gradient_functions(func_graph, renamed_functions, loaded_gradients)

    for dep in function_deps[orig_name]:
        functions[dep].add_to_graph(func_graph)

    # We do not initialize the new ConcreteFunction's function_spec and/or
    # arg_keywords here (which are used to parse the structured and flat
    # signatures, respectively). ConcreteFunction that are part of a saved
    # function is set up later by recreate_function(); and bare ConcreteFunction
    # is set up by by setup_bare_concrete_function().
    # However, we copy the FunctionDef attributes to the new ConcreteFunction,
    # excluding the "_input_shapes", which may cause an error during input shape
    # initialization at a later stage.
    if "_input_shapes" in fdef.attr:
        del fdef.attr["_input_shapes"]
    func = function_lib.ConcreteFunction(func_graph, attrs=fdef.attr)
    if wrapper_function:
        func = wrapper_function(func)
    func.add_to_graph(graph)

    functions[orig_name] = func
    renamed_functions[func.name] = func
    if any(op.type == "TRTEngineOp" for op in func_graph.get_operations()):
        # TODO(b/150708051): Remove this hack once TensorRT SavedModel integration
        # is fixed. Currently it's leaking memory to maintain bug compatibility
        # with previous behavior.
        func.add_to_graph(ops.get_default_graph())

    if orig_name in gradients_to_register:
        gradient_op_type = gradients_to_register[orig_name]
        loaded_gradients[compat.as_bytes(gradient_op_type)] = func
        ops.RegisterGradient(gradient_op_type)(_gen_gradient_func(func))

exit(functions)
