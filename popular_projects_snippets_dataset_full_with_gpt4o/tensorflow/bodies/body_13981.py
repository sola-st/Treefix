# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
super(_WhileBodyGradFuncGraph, self).__init__(name)
self.extra_inputs = []
self.internal_capture_to_output = {}
# FuncGraph for the body of the forward While op.
self._forward_graph = forward_body_graph
# FuncGraph for the cond of the forward While op.
self._forward_cond_graph = forward_cond_graph
self._maximum_iterations = maximum_iterations
self._forward_while_op = forward_while_op
# Dict from forward intermediate tensor to its indirectly captured tensor
# in this graph. Indirect capturing happens in two ways:
# 1. For non-resource tensors we capture their accumulators from the forward
#    outer graph and pop values from that accumulator inside this graph
#    using TensorListPopBack.
# 2. For resource tensors we directly capture their corresponding tensor
#    in the forward outer graph.
self._indirect_captures = {}
