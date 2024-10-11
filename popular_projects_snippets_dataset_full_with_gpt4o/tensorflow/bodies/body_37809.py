# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
k, v = self.evaluate([key, value])
self.assertAllEqual(compat.as_bytes(self._filenames[index]), k)
self.assertAllEqual(self._content[index], v)
