# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
"""Constructor of EventListenerTestServicer.

    Args:
      server_port: (int) The server port number.
      dump_dir: (str) The root directory to which the data files will be
        dumped. If empty or None, the received debug data will not be dumped
        to the file system: they will be stored in memory instead.
      toggle_watch_on_core_metadata: A list of
        (node_name, output_slot, debug_op) tuples to toggle the
        watchpoint status during the on_core_metadata calls (optional).
    """
self.core_metadata_json_strings = []
self.partition_graph_defs = []
self.debug_tensor_values = collections.defaultdict(list)
self._initialize_toggle_watch_state(toggle_watch_on_core_metadata)

grpc_debug_server.EventListenerBaseServicer.__init__(
    self, server_port,
    functools.partial(EventListenerTestStreamHandler, dump_dir, self))

# Members for storing the graph ops traceback and source files.
self._call_types = []
self._call_keys = []
self._origin_stacks = []
self._origin_id_to_strings = []
self._graph_tracebacks = []
self._graph_versions = []
self._source_files = []
