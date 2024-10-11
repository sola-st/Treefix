# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors.py
"""Monitor method for top-level execution events.

    Return values (if any) are ignored by the associated DebugDataReader.

    Args:
      execution_index: The index of the top-level execution event, as an int.
      execution: An Execution data object, for a top-level op or function
        execution event.
    """
