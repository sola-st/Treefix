# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
self._event_listener_servicer.toggle_watch()

core_metadata = json.loads(event.log_message.message)

if not self._grpc_path:
    grpc_path = core_metadata["grpc_path"]
    if grpc_path:
        if grpc_path.startswith("/"):
            grpc_path = grpc_path[1:]
    if self._dump_dir:
        self._dump_dir = os.path.join(self._dump_dir, grpc_path)

        # Write cached graph defs to filesystem.
        for graph_def, device_name, wall_time in zip(
            self._cached_graph_defs,
            self._cached_graph_def_device_names,
            self._cached_graph_def_wall_times):
            self._write_graph_def(graph_def, device_name, wall_time)

if self._dump_dir:
    self._write_core_metadata_event(event)
else:
    self._event_listener_servicer.core_metadata_json_strings.append(
        event.log_message.message)
