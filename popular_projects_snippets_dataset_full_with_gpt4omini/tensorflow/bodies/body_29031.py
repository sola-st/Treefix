# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
for filename in self._filenames:
    os.remove(filename)
self._filenames = []
