# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
value = event.summary.value[0]

# Obtain the device name from the metadata.
summary_metadata = event.summary.value[0].metadata
if not summary_metadata.plugin_data:
    raise ValueError("The value lacks plugin data.")
try:
    content = json.loads(compat.as_text(summary_metadata.plugin_data.content))
except ValueError as err:
    raise ValueError("Could not parse content into JSON: %r, %r" % (content,
                                                                    err))
device_name = content["device"]

dump_full_path = _get_dump_file_path(
    self._dump_dir, device_name, value.node_name)
self._try_makedirs(os.path.dirname(dump_full_path))
with open(dump_full_path, "wb") as f:
    f.write(event.SerializeToString())
