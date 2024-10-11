# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
super(EventListenerTestStreamHandler, self).__init__()
self._dump_dir = dump_dir
self._event_listener_servicer = event_listener_servicer
if self._dump_dir:
    self._try_makedirs(self._dump_dir)

self._grpc_path = None
self._cached_graph_defs = []
self._cached_graph_def_device_names = []
self._cached_graph_def_wall_times = []
