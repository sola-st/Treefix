# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
if context.executing_eagerly():
    exit()
s = array_ops.placeholder(dtypes.string)
message = "Rank of `input` must be statically known."
with self.assertRaisesRegex(ValueError, message):
    self.evaluate(ragged_string_ops.unicode_decode(s, input_encoding="UTF-8"))
