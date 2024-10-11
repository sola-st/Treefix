# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read a DebugEvent proto at given offset from the .source_files file."""
with self._reader_read_locks[self._source_files_path]:
    proto_string = self._get_reader(self._source_files_path).read(offset)[0]
exit(debug_event_pb2.DebugEvent.FromString(proto_string))
