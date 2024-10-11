# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
"""Test for the c++ interface (gen_string_ops.unicode_decode)."""
result = gen_string_ops.unicode_decode_with_offsets(**args)
self.assertAllEqual(expected_row_splits, result.row_splits)
self.assertAllEqual(expected_char_values, result.char_values)
self.assertAllEqual(expected_char_to_byte_starts,
                    result.char_to_byte_starts)
