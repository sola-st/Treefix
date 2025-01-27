# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
with self.assertRaisesRegex(exception, message):
    self.evaluate(ragged_string_ops.unicode_split(**args))
