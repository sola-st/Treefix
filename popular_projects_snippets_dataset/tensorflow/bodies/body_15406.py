# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
x = ragged_tensor.convert_to_tensor_or_ragged_tensor(x, dtype=dtypes.int32)
y = ragged_tensor.convert_to_tensor_or_ragged_tensor(y, dtype=dtypes.int32)
result = x + y
self.assertAllEqual(result, expected)
self.assertEqual(result.row_splits.dtype, expected_row_splits_dtype)
