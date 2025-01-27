# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
words = ["string1", "string2"]

observed = self._decode_v1(words)
expected = self._ordinalize(words)

self.assertAllEqual(expected.shape, observed.shape)
self.assertAllEqual(expected, observed)
