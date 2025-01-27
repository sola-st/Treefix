# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
words = ["string", "longer_string"]
with self.assertRaises(errors_impl.InvalidArgumentError):
    self._decode_v2(words)
