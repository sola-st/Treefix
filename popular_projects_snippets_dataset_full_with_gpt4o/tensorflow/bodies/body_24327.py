# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors.py
"""Monitor method for intra-graph execution events.

    Return values (if any) are ignored by the associated DebugDataReader.

    Args:
      graph_execution_trace_index: The index of the intra-graph execution
        event, as an int.
      graph_execution_trace: A GraphExecutionTrace data object, for an
        intra-graph tensor event.
    """
