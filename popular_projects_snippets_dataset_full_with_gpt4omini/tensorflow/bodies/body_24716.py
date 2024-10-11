# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Load the dump data for all devices."""
device_dirs = _glob(os.path.join(
    self._dump_root, METADATA_FILE_PREFIX + DEVICE_TAG + "*"))

self._device_names = []
self._t0s = {}
self._dump_tensor_data = {}
self._dump_graph_file_paths = {}
self._debug_watches = {}
self._watch_key_to_devices = {}
self._watch_key_to_datum = {}
self._watch_key_to_rel_time = {}
self._watch_key_to_dump_size_bytes = {}
for device_dir in device_dirs:
    device_name = device_path_to_device_name(device_dir)
    self._device_names.append(device_name)
    self._load_device_dumps(device_name, device_dir)
self._load_partition_graphs(partition_graphs, validate)
self._calculate_t0()

for device_name in self._device_names:
    self._create_tensor_watch_maps(device_name)
