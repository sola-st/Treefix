# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
k, v = self.evaluate([key, value])
self.assertAllEqual(expected, k)
self.assertAllEqual(expected, v)
