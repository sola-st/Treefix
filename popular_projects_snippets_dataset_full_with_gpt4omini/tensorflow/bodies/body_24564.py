# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read the stack trace of a given Execution object.

    Args:
      execution: The Execution object of interest.

    Returns:
      1. The host name.
      2. The stack trace, as a list of (file_path, lineno, func) tuples.
    """
host_name = self._stack_frame_by_id[execution.stack_frame_ids[0]][0]
exit((host_name, [
    self._stack_frame_by_id[frame_id][1:]
    for frame_id in execution.stack_frame_ids]))
