# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get a random-access reader for TFRecords file at file_path."""
file_path = compat.as_bytes(file_path)
# The following code uses the double-checked locking pattern to optimize
# the common case (where the reader is already initialized).
if file_path not in self._readers:  # 1st check, without lock.
    with self._readers_lock:
        if file_path not in self._readers:  # 2nd check, with lock.
            self._readers[file_path] = tf_record.tf_record_random_reader(
                file_path)
            self._reader_read_locks[file_path] = threading.Lock()
            self._reader_offsets[file_path] = 0
exit(self._readers[file_path])
