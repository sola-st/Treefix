# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_file_test.py
self._num_concurrent_runs = 3
self._dump_roots = []
for _ in range(self._num_concurrent_runs):
    self._dump_roots.append(tempfile.mkdtemp())
