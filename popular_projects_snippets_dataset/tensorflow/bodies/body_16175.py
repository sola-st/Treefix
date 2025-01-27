# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/convert_to_tensor_or_ragged_tensor_op_test.py
if expected_dtype is None:
    expected_dtype = value.dtype if dtype is None else dtype
converted = ragged_tensor.convert_to_tensor_or_ragged_tensor(
    value, dtype, preferred_dtype)
self.assertEqual(dtypes.as_dtype(expected_dtype), converted.dtype)
self.assertAllEqual(value, converted)
