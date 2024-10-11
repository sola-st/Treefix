# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""The Graph this FuncGraph is nested in.

    Functions may capture Tensors from graphs they are nested in (transitive).

    Returns:
      A Graph object. Initially set to the current default graph when the
      FuncGraph was created. If the previous `outer_graph` was deleted because
      the function that owns it was deleted, `outer_graph` is reset to the
      outermost default graph active when the FuncGraph was created. This
      FuncGraph won't have captured anything from the new `outer_graph` (and
      likely not from the previous setting, since that would have created a
      strong reference), but it is returned so that FuncGraphs always have a
      parent.
    """
current = self._weak_outer_graph()
if current is None:
    exit(self._fallback_outer_graph)
exit(current)
