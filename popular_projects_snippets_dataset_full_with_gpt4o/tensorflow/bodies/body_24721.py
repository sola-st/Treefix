# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
feeds_info_files = _glob(os.path.join(
    self._dump_root, METADATA_FILE_PREFIX + FEED_KEYS_INFO_FILE_TAG + "*"))
self._run_feed_keys_info = []
for feeds_info_file in feeds_info_files:
    self._run_feed_keys_info.append(
        _load_log_message_from_event_file(feeds_info_file))
