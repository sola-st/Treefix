# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
self._toggle_watches = toggle_watches
self._toggle_watch_state = {}
if self._toggle_watches:
    for watch_key in self._toggle_watches:
        self._toggle_watch_state[watch_key] = False
