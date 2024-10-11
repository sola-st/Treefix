# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
for watch_key in self._toggle_watch_state:
    node_name, output_slot, debug_op = watch_key
    if self._toggle_watch_state[watch_key]:
        self.request_unwatch(node_name, output_slot, debug_op)
    else:
        self.request_watch(node_name, output_slot, debug_op)
    self._toggle_watch_state[watch_key] = (
        not self._toggle_watch_state[watch_key])
