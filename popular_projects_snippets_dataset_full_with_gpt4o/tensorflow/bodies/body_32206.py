# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
input_tensor = ragged_factory_ops.constant_value(
    _nested_encode(texts, "UTF-8"), ragged_rank=ragged_rank, dtype=bytes)
result = ragged_string_ops.unicode_split_with_offsets(input_tensor, "UTF-8")
expected_codepoints = _nested_splitchars(texts, "UTF-8")
expected_offsets = _nested_offsets(texts, "UTF-8")
self.assertAllEqual(expected_codepoints, result[0])
self.assertAllEqual(expected_offsets, result[1])
