# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
if context.executing_eagerly():
    exit(self)
# This code assumes no other thread is adding ops to the graph while
# we're adding ops to the graph.
# TODO(apassos): Fix this by locking the graph or using a temporary
# graph (but that would mess up devices and collections at least,
# probably other things as well).
g = ops.get_default_graph()
self._graph = g
g._add_control_dependencies = True  # pylint: disable=protected-access
g.experimental_acd_manager = self
self._n_operations = len(g.get_operations())
exit(self)
