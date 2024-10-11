# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
self.core_metadata_json_strings = []
self.partition_graph_defs = []
self.debug_tensor_values = collections.defaultdict(list)
self._call_types = []
self._call_keys = []
self._origin_stacks = []
self._origin_id_to_strings = []
self._graph_tracebacks = []
self._graph_versions = []
self._source_files = []
