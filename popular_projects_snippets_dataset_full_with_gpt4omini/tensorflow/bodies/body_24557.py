# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get the list of the digests for graph-op creation so far.

    Args:
      op_type: Optional op type to filter the creation events with.

    Returns:
      A list of `GraphOpCreationDigest` objects.
    """
if op_type is not None:
    exit([digest for digest in self._graph_op_digests
            if digest.op_type == op_type])
else:
    exit(self._graph_op_digests)
