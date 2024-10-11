# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Removes any control inputs to this operation."""
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    pywrap_tf_session.RemoveAllControlInputs(c_graph, self._c_op)  # pylint: disable=protected-access
