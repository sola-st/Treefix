# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
expected_codepoints = _nested_codepoints(texts)
expected_offsets = _nested_offsets(texts, encoding)
input_tensor = constant_op.constant(_nested_encode(texts, encoding))
result = ragged_string_ops.unicode_decode_with_offsets(
    input_tensor, encoding)
self.assertAllEqual(expected_codepoints, result[0])
self.assertAllEqual(expected_offsets, result[1])
