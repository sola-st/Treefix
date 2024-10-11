# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph.py
"""Converts a FunctionDef to a FuncGraph (sub-class Graph).

  The returned FuncGraph's `name`, `inputs` and `outputs` fields will be set.
  The input tensors are represented as placeholders.

  Note: `FuncGraph.inputs` and `FuncGraph.captures` are not set and may be set
  by the caller.

  Args:
    fdef: FunctionDef.
    structured_input_signature: Optional. The structured input signature to
      use for initializing the FuncGraph. See the docstring for FuncGraph for
      more information.
    structured_outputs: Optional. The structured outputs to use for
      initializing the FuncGraph. See the docstring for FuncGraph for more
      information.
    input_shapes: Optional. A list of TensorShape objects of the shapes of
      function inputs. Defaults to the function's "_input_shapes" attribute. If
      specified, its length must match length of `fdef.signature.input_arg`. If
      a shape is None, the corresponding input placeholder will have unknown
      shape.
    propagate_device_spec: Optional. Whether to propagate assigned device
      information when constructing a new Graph from a FunctionDef.

  Returns:
    A FuncGraph.
  """
func_graph = FuncGraph(fdef.signature.name,
                       structured_input_signature=structured_input_signature,
                       structured_outputs=structured_outputs)
if input_shapes is None:
    input_shapes_attr = fdef.attr.get("_input_shapes", None)
    if input_shapes_attr is not None:
        raw_input_shapes = input_shapes_attr.list.shape

        # Replace resource handle shapes in the inputs to disable shape inference.
        # Setting the shape to either the variable handle shape (which is always
        # `[]`) or the variable shape can cause shape inference issues.
        input_shapes = []
        for input_shape, arg_def in zip(raw_input_shapes,
                                        fdef.signature.input_arg):
            if arg_def.type == types_pb2.DT_RESOURCE and arg_def.handle_data:
                input_shapes.append(None)
            else:
                input_shapes.append(input_shape)

graph_def, nested_to_flat_tensor_name = function_def_to_graph_def(
    fdef, input_shapes)

with func_graph.as_default():
    # Add all function nodes to the graph.
    importer.import_graph_def_for_function(
        graph_def, name="", propagate_device_spec=propagate_device_spec)

    # Initialize fields specific to FuncGraph.

    # inputs
    input_tensor_names = [
        nested_to_flat_tensor_name[arg.name] for arg in fdef.signature.input_arg
    ]
    func_graph.inputs = [
        func_graph.get_tensor_by_name(name) for name in input_tensor_names
    ]

    # outputs
    output_tensor_names = [
        nested_to_flat_tensor_name[fdef.ret[arg.name]]
        for arg in fdef.signature.output_arg
    ]
    func_graph.outputs = [
        func_graph.get_tensor_by_name(name) for name in output_tensor_names
    ]
    func_graph.control_outputs = [
        func_graph.get_operation_by_name(fdef.control_ret[ret_name])
        for ret_name in fdef.signature.control_output
    ]

    _set_handle_data(func_graph, fdef)

    for node in graph_def.node:
        output_shapes = node.attr.get("_output_shapes", None)
        if output_shapes is not None:
            op = func_graph.get_operation_by_name(node.name)
            # _output_shapes for functions can sometimes be too long because the
            # output-intermediates-for-gradients version of the function was
            # substituted before saving. We'll accept that here. (See b/133666530).
            for output_index, shape in enumerate(
                output_shapes.list.shape[:len(op.outputs)]):
                op.outputs[output_index].set_shape(shape)
    output_names = {}
    for ret_arg_def, tensor_name in zip(
        fdef.signature.output_arg, output_tensor_names):
        output_names[ops.tensor_id(
            func_graph.get_tensor_by_name(tensor_name))] = (
                ret_arg_def.name)
    func_graph._output_names = output_names  # pylint: disable=protected-access
exit(func_graph)
