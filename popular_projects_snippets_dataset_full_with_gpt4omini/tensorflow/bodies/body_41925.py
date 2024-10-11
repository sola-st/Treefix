# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Registers the function, adds it to the graph g or default graph.

    Args:
      g: If specified, registers the function with this graph. Defaults to the
        current context (either the default graph or the eager context).
      overwrite: A bool. If True, its forward function will overwrite
        any existing function of the same signature name in the graph `g`.
    """
# If we are not executing eagerly, adds the function to default graph if no
# graph is specified.
# In case of eager execution, function definition gets added to context
# during construction itself.

if not context.executing_eagerly() and not g:
    g = ops.get_default_graph()
self._delayed_rewrite_functions.forward().add_to_graph(g, overwrite)
