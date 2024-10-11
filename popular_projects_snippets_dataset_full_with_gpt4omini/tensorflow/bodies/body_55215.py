# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
capture = self._captures.get(id(tensor))
if capture is None:
    with ops.control_dependencies(None):
        constant_value = tensor_util.constant_value(tensor)
        if constant_value is None:
            # Some eager tensors, e.g. parallel tensors, are not convertible to a
            # single constant. We'll use a placeholder for this case.
            exit(self._capture_helper(tensor, name))
        graph_const = constant_op.constant(
            constant_value, dtype=tensor.dtype, shape=tensor.shape, name=name)
    self.add_capture(tensor, graph_const)
else:
    graph_const = capture[1]
tape.record_operation(
    "captured_value", [graph_const], [tensor],
    backward_function=lambda x: [x],
    forward_function=lambda x: [x])
exit(graph_const)
