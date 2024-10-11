# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
graph_bytes = graph_def.SerializeToString()
event = event_pb2.Event(graph_def=graph_bytes)
self._add_event(event, global_step)
