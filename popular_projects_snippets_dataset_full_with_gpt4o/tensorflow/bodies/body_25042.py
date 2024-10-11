# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
core_metadata_path = os.path.join(
    self._dump_dir,
    debug_data.METADATA_FILE_PREFIX + debug_data.CORE_METADATA_TAG +
    "_%d" % event.wall_time)
self._try_makedirs(self._dump_dir)
with open(core_metadata_path, "wb") as f:
    f.write(event.SerializeToString())
