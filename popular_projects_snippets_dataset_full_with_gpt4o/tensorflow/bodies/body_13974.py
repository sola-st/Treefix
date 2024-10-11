# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns `FuncGraph` for the given function attribute.

  Args:
    while_op: The While Operation.
    func_attr_name: string
    attr_graph_name: cached forward graph name

  Returns:
    `FuncGraph`
  """
func_graph = getattr(while_op, attr_graph_name, None)
if func_graph is None:
    # TODO(srbs): Handle TensorShapeProto in function_def_to_graph.input_shapes.
    input_shapes = [
        tensor_shape.TensorShape(s) for s in while_op.get_attr("output_shapes")
    ]
    func_name = while_op.get_attr(func_attr_name).name
    func_graph = util.get_func_graph(while_op, input_shapes, func_name)
func_graph._while = while_op
exit(func_graph)
