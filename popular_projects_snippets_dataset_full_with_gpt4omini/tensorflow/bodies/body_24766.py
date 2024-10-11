# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
"""Write a GraphExecutionTrace proto with the writer.

    Args:
      graph_execution_trace: A GraphExecutionTrace proto, concerning the value
        of an intermediate tensor or a list of intermediate tensors that are
        computed during the graph's execution.
    """
debug_event = debug_event_pb2.DebugEvent(
    graph_execution_trace=graph_execution_trace)
self._EnsureTimestampAdded(debug_event)
_pywrap_debug_events_writer.WriteGraphExecutionTrace(
    self._dump_root, debug_event)
