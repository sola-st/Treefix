# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
if not file_io.is_directory(dump_root):
    raise ValueError("Specified dump_root is not a directory: %s" % dump_root)
self._dump_root = dump_root
self._metadata_paths = self._load_metadata_files()

prefixes = [
    metadata_path[:-len(self._METADATA_SUFFIX)]
    for metadata_path in self._metadata_paths
]
prefix = prefixes[0]  # This is the prefix of the main file set.
self._source_files_path = compat.as_bytes(prefix + self._SOURCE_FILE_SUFFIX)
self._stack_frames_path = compat.as_bytes(prefix +
                                          self._STACK_FRAMES_SUFFIX)
self._graphs_path = compat.as_bytes(prefix + self._GRAPHS_SUFFIX)
self._execution_path = compat.as_bytes(prefix + self._EXECUTION_SUFFIX)
# There can be multiple .graph_execution_trace files each belonging
# to a file set generated on an individual host, in the case of
# a distributed TensorFlow job.
# This is different from the other debug event files in the file set.
self._graph_execution_traces_paths = [
    compat.as_bytes(prefix + self._GRAPH_EXECUTION_TRACES_SUFFIX)
    for prefix in prefixes
]
self._readers = dict()  # A map from file path to reader.
# A map from file path to current reading offset.
self._reader_offsets = dict()
# Lock for reader creation.
self._readers_lock = threading.Lock()
# Locks for read operation on individual readers.
self._reader_read_locks = dict()

self._offsets = dict()
