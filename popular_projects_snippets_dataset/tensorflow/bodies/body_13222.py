# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
super(_CondGradFuncGraph, self).__init__(
    name, collections=ops.get_default_graph()._collections)  # pylint: disable=protected-access
self.op_needs_rewrite = False
self._forward_graph = forward_graph
# Maps from forward intermediate tensor -> the unwrapped captured
# intermediate.
self._indirect_captures = {}
# Maps unwrapped intermediate -> optional-wrapped intermediate in the
# forward graph.
self._wrapped_intermediates = collections.OrderedDict()
# Raw intermediates captured from the forward graph. Populated iff we're in
# an XLA context.
self._xla_intermediates = []
# Maps forward intermediate constant valued tensor's id to the constant
# created in this graph for that tensor.
self._captured_constants = {}
