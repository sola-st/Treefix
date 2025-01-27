# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
words = ["string", "longer_string"]

observed = self._decode_v2(words, fixed_length=8)
expected = self._ordinalize(words, fixed_length=8)

self.assertAllEqual(expected.shape, observed.shape)
self.assertAllEqual(expected, observed)
