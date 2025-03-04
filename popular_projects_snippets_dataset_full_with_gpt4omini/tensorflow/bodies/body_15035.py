# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
splits1 = [0, 2, 2, 5, 6, 7]
splits2 = np.array([0, 2, 2, 5, 6, 7], np.int64)
splits3 = np.array([0, 2, 2, 5, 6, 7], np.int32)
splits4 = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
splits5 = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int32)
rt1 = RaggedTensor.from_row_splits(values, splits1)
rt2 = RaggedTensor.from_row_splits(values, splits2)
rt3 = RaggedTensor.from_row_splits(values, splits3)
rt4 = RaggedTensor.from_row_splits(values, splits4)
rt5 = RaggedTensor.from_row_splits(values, splits5)
self.assertEqual(rt1.row_splits.dtype, dtypes.int64)
self.assertEqual(rt2.row_splits.dtype, dtypes.int64)
self.assertEqual(rt3.row_splits.dtype, dtypes.int32)
self.assertEqual(rt4.row_splits.dtype, dtypes.int64)
self.assertEqual(rt5.row_splits.dtype, dtypes.int32)
