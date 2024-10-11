# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
expected = _nested_splitchars(texts, encoding)
input_tensor = constant_op.constant(_nested_encode(texts, encoding))
result = ragged_string_ops.unicode_split(input_tensor, encoding)
self.assertAllEqual(expected, result)
