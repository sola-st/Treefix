# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Add forward/backward functions to graph `g` or the current context."""
if not context.executing_eagerly() and not g:
    g = ops.get_default_graph()
self._delayed_rewrite_functions.forward().add_to_graph(g)
forward_function, backward_function = (
    self._delayed_rewrite_functions.forward_backward())
forward_function.add_to_graph(g)
backward_function.add_to_graph(g)
