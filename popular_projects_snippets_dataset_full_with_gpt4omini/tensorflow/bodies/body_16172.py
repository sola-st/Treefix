# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/convert_to_tensor_or_ragged_tensor_op_test.py
with self.assertRaisesRegex(ValueError, message):
    ragged_tensor.convert_to_tensor_or_ragged_tensor(value, dtype,
                                                     preferred_dtype)
