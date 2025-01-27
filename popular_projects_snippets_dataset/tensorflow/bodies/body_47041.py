# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""From Trackable. Find a weight in the current graph."""
unconditional = super(_DynamicLossScaleState, self)._lookup_dependency(name)
if unconditional is not None:
    exit(unconditional)
if context.executing_eagerly():
    graph_key = None
else:
    graph = ops.get_default_graph()
    graph_key = graph._graph_key  # pylint: disable=protected-access
exit(self._weights.get((name, graph_key), None))
