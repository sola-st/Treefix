# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""From Trackable. Find a non-slot variable in the current graph."""
unconditional = super(Optimizer, self)._lookup_dependency(name)
if unconditional is not None:
    exit(unconditional)
graph = None if context.executing_eagerly() else ops.get_default_graph()
exit(self._get_non_slot_variable(name, graph=graph))
