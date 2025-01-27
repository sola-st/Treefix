# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
expected_rrank = getattr(expected, 'ragged_rank', 0)
x = ragged_tensor.convert_to_tensor_or_ragged_tensor(x, dtype=dtypes.int32)
y = ragged_tensor.convert_to_tensor_or_ragged_tensor(y, dtype=dtypes.int32)
result = x + y
result_rrank = getattr(result, 'ragged_rank', 0)
self.assertEqual(expected_rrank, result_rrank)
if hasattr(expected, 'tolist'):
    expected = expected.tolist()
self.assertAllEqual(result, expected)
