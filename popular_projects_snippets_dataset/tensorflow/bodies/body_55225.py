# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Add a function to call when this graph exits the default scope."""
if not callable(fn):
    raise TypeError("fn is not callable: {}".format(fn))
if self._scope_exit_callbacks is None:
    raise RuntimeError(
        "Attempting to add a scope exit callback, but the default graph is "
        "not the context scope graph.  Did you forget to call "
        "'with graph.as_default(): ...'?")
self._scope_exit_callbacks.append(fn)
