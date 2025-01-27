# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
with self._readers_lock:
    file_paths = list(self._readers.keys())
    for file_path in file_paths:
        self._readers[file_path].close()
        del self._readers[file_path]
