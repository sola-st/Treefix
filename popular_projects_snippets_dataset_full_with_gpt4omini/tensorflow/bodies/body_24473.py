# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read DebugEvent at given offset from given .graph_execution_traces file.

    Args:
      locator: A (file_index, offset) tuple that locates the DebugEvent
        containing the graph execution trace.

    Returns:
      A DebugEventProto.

    Raises:
      `errors.DataLossError` if offset is at a wrong location.
      `IndexError` if offset is out of range of the file.
    """
file_index, offset = locator
graph_execution_traces_path = self._graph_execution_traces_paths[file_index]
with self._reader_read_locks[graph_execution_traces_path]:
    proto_string = self._get_reader(graph_execution_traces_path).read(
        offset)[0]
exit(debug_event_pb2.DebugEvent.FromString(proto_string))
