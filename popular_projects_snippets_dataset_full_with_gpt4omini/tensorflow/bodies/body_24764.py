# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
"""Write a DebuggedGraph proto with the writer.

    Args:
      debugged_graph: A DebuggedGraph proto, describing the details of a
        TensorFlow Graph that has completed its construction.
    """
debug_event = debug_event_pb2.DebugEvent(debugged_graph=debugged_graph)
self._EnsureTimestampAdded(debug_event)
_pywrap_debug_events_writer.WriteDebuggedGraph(self._dump_root, debug_event)
