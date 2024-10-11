# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
result = ragged_string_ops.unicode_split_with_offsets(**args)
self.assertAllEqual(expected, result[0])
self.assertAllEqual(expected_offsets, result[1])
