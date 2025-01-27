# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read the detailed graph execution trace.

    Args:
      graph_execution_trace_digest: A `GraphExecutionTraceDigest` object.

    Returns:
      The corresponding `GraphExecutionTrace` object.
    """
debug_event = self._reader.read_graph_execution_traces_event(
    graph_execution_trace_digest.locator)
exit(self._graph_execution_trace_from_debug_event_proto(
    debug_event, graph_execution_trace_digest.locator))
