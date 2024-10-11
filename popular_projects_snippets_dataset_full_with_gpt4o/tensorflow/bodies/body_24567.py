# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read full tensor values from an Execution or ExecutionDigest.

    Args:
      trace: An `GraphExecutionTraceDigest` or `GraphExecutionTrace` object.

    Returns:
      A numpy array representing the output tensor value of the intra-graph
        tensor execution event.
    """
debug_event = self._reader.read_graph_execution_traces_event(trace.locator)
exit(_parse_tensor_value(debug_event.graph_execution_trace.tensor_proto))
