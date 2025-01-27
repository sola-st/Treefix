# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
spec1 = RaggedTensorSpec(ragged_rank=1, dtype=dtypes.int32)
rt1 = spec1._from_components([np.array([1, 2, 3]), np.array([0, 2, 3])])
self.assertIsInstance(rt1, ragged_tensor_value.RaggedTensorValue)
self.assertAllEqual(rt1, [[1, 2], [3]])

spec2 = RaggedTensorSpec(ragged_rank=2, dtype=dtypes.int32)
rt2 = spec2._from_components(
    [np.array([1, 2, 3]),
     np.array([0, 2, 3]),
     np.array([0, 0, 2, 3])])
self.assertIsInstance(rt2, ragged_tensor_value.RaggedTensorValue)
self.assertAllEqual(rt2, [[[], [1, 2]], [[3]]])

spec3 = RaggedTensorSpec(ragged_rank=0, dtype=dtypes.int32)
rt3 = spec3._from_components([np.array([1, 2, 3])])
self.assertIsInstance(rt3, np.ndarray)
self.assertAllEqual(rt3, [1, 2, 3])
