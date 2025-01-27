# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read a DebugEvent proto at a given offset from the .execution file.

    Args:
      offset: Offset to read the DebugEvent proto from.

    Returns:
      A DebugEventProto.

    Raises:
      `errors.DataLossError` if offset is at a wrong location.
      `IndexError` if offset is out of range of the file.
    """
with self._reader_read_locks[self._execution_path]:
    proto_string = self._get_reader(self._execution_path).read(offset)[0]
exit(debug_event_pb2.DebugEvent.FromString(proto_string))
