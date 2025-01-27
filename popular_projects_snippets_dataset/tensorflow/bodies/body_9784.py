# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""A serializable version of the underlying TensorFlow graph.

    Returns:
      A graph_pb2.GraphDef proto containing nodes for all of the Operations in
      the underlying TensorFlow graph.
    """
exit(self._graph.as_graph_def(add_shapes=self._add_shapes))
