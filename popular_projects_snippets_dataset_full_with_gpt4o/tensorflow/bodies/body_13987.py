# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns the captured resource tensor.

    Resource-type tensors are not accumulated. If a resource tensor exists in
    the loop body it must either be a loop input or an output of a nested While
    op inside the loop body which had captured the external resource.

    Args:
      tensor: the external resource Tensor to be captured.

    Returns:
      Tensor in this graph.
    """
assert tensor.dtype == dtypes.resource

forward_graph_input_names = [t.name for t in self._forward_graph.inputs]
forward_graph_name_to_opdef = {
    op.name: op.node_def for op in self._forward_graph.get_operations()}
index = util.resource_input_index(
    tensor.name, forward_graph_input_names,
    forward_graph_name_to_opdef,
    self._forward_graph._functions)

input_placeholder = self._forward_graph.inputs[index]
tensor_in_outer_graph = self._forward_graph._while.inputs[index]

assert input_placeholder.dtype == dtypes.resource
assert tensor_in_outer_graph.dtype == dtypes.resource
# This must be a loop invariant. However, infrastructure
# (e.g. tf.vectorized_map) may insert identity nodes, function calls, conds,
# etc. which take and return the resource tensor unmodified; this means that
# the Python objects may differ.
if index != util.resource_input_index(
    self._forward_graph.outputs[index].name, forward_graph_input_names,
    forward_graph_name_to_opdef,
    self._forward_graph._functions):
    raise AssertionError(
        f"Resource tensors must be loop invariants {tensor_in_outer_graph}")

self._indirect_captures[ops.tensor_id(tensor)] = self.capture(
    tensor_in_outer_graph)
exit(self._indirect_captures[ops.tensor_id(tensor)])
