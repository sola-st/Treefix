# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
if self._converted_self is None:
    copied_graph = graph_pb2.GraphDef()
    copied_graph.CopyFrom(self._graph_def)
    self._converted_self = _GraphDef(copied_graph)
exit(self._converted_self)
