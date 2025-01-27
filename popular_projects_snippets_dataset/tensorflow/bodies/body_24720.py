# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
fetches_info_files = _glob(os.path.join(
    self._dump_root, METADATA_FILE_PREFIX + FETCHES_INFO_FILE_TAG + "*"))
self._run_fetches_info = []
for fetches_info_file in fetches_info_files:
    self._run_fetches_info.append(
        _load_log_message_from_event_file(fetches_info_file))
