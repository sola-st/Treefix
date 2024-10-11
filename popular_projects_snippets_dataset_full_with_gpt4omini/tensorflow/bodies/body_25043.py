# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
encoded_graph_def = graph_def.SerializeToString()
graph_hash = int(hashlib.sha1(encoded_graph_def).hexdigest(), 16)
event = event_pb2.Event(graph_def=encoded_graph_def, wall_time=wall_time)
graph_file_path = os.path.join(
    self._dump_dir,
    debug_data.device_name_to_device_path(device_name),
    debug_data.METADATA_FILE_PREFIX + debug_data.GRAPH_FILE_TAG +
    debug_data.HASH_TAG + "%d_%d" % (graph_hash, wall_time))
self._try_makedirs(os.path.dirname(graph_file_path))
with open(graph_file_path, "wb") as f:
    f.write(event.SerializeToString())
