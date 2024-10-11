# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
input_tensor = ragged_factory_ops.constant_value(
    _nested_encode(texts, "UTF-8"), ragged_rank=ragged_rank, dtype=bytes)
result = ragged_string_ops.unicode_decode(
    input_tensor, "UTF-8").to_tensor(default_value=-1)
self.assertAllEqual(expected, result)
