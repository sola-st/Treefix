# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
"""Write a GraphOpCreation proto with the writer.

    Args:
      graph_op_creation: A GraphOpCreation proto, describing the details of the
        creation of an op inside a TensorFlow Graph.
    """
debug_event = debug_event_pb2.DebugEvent(
    graph_op_creation=graph_op_creation)
self._EnsureTimestampAdded(debug_event)
_pywrap_debug_events_writer.WriteGraphOpCreation(self._dump_root,
                                                 debug_event)
