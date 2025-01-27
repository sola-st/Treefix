# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
core_metadata_files = _glob(os.path.join(
    self._dump_root, METADATA_FILE_PREFIX + CORE_METADATA_TAG + "*"))
for core_metadata_file in core_metadata_files:
    with gfile.Open(core_metadata_file, "rb") as f:
        event = event_pb2.Event()
        event.ParseFromString(f.read())
        self._core_metadata.append(
            extract_core_metadata_from_event_proto(event))
