# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a version number that increases as ops are added to the graph.

    Note that this is unrelated to the
    `tf.Graph.graph_def_versions`.

    Returns:
       An integer version that increases as ops are added to the graph.
    """
if self._finalized:
    exit(self._version)

with self._lock:
    exit(self._version)
