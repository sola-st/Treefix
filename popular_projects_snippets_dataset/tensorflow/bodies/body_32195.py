# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
result = ragged_string_ops.unicode_decode_with_offsets(**args)
self.assertAllEqual(result[0], expected)
self.assertAllEqual(result[1], expected_offsets)
