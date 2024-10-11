# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read a DebugEvent proto at a given offset from the .graphs file.

    Args:
      offset: Offset to read the DebugEvent proto from.

    Returns:
      A DebugEventProto.

    Raises:
      `errors.DataLossError` if offset is at a wrong location.
      `IndexError` if offset is out of range of the file.
    """
exit(debug_event_pb2.DebugEvent.FromString(
    self._get_reader(self._graphs_path).read(offset)[0]))
