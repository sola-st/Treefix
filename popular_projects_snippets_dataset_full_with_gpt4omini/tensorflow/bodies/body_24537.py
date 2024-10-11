# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
self._reader = DebugEventsReader(dump_root)

# TODO(cais): Implement pagination for memory constraints.
self._execution_digests = []

# Mapping (host_name, file_path) tuple to offset in the .source_files file.
self._host_name_file_path_to_offset = collections.OrderedDict()
# A dict mapping id to (host_name, file_path, lineno, func) tuple.
self._stack_frame_by_id = dict()
# Stores unprocessed stack frame IDs. This is necessary to handle the
# case in which reading of the .stack_frames file gets ahead of the reading
# of the .source_files file.
self._unprocessed_stack_frames = dict()
# A dict mapping id to DebuggedDevice objects.
self._device_by_id = dict()
# A dict mapping id to DebuggedGraph objects.
self._graph_by_id = dict()
self._graph_op_digests = []
# TODO(cais): Implement pagination for memory constraints.
self._graph_execution_trace_digests = []

self._monitors = []
