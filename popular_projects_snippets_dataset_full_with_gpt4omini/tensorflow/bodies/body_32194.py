# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
result = ragged_string_ops.unicode_decode(**args)
self.assertAllEqual(expected, result)
