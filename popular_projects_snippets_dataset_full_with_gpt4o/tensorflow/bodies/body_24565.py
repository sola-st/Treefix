# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read the stack trace of a given graph op creation object.

    Args:
      graph_op_creation_digest: The GraphOpCreationDigest object of interest.

    Returns:
      A tuple consisting of:
        1. The host name.
        2. The stack trace, as a list of (file_path, lineno, func) tuples.
    """
exit((graph_op_creation_digest.host_name, [
    self._stack_frame_by_id[frame_id][1:]
    for frame_id in graph_op_creation_digest.stack_frame_ids
]))
