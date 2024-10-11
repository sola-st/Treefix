# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Private method used to clear an attribute in the node_def."""
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    # pylint: disable=protected-access
    pywrap_tf_session.ClearAttr(c_graph, self._c_op, attr_name)
    # pylint: enable=protected-access
