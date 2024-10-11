# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""From Trackable. Gather graph-specific weights to save."""
if context.executing_eagerly():
    graph_key = None
else:
    graph = ops.get_default_graph()
    graph_key = graph._graph_key  # pylint: disable=protected-access
weights = {}
for (name, g), v in sorted(self._weights.items(), key=lambda i: i[0][0]):
    if g == graph_key:
        weights[name] = v
weights.update(
    super(LossScale, self)._trackable_children(save_type, **kwargs))
exit(weights)
