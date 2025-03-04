# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
splits1 = [0, 2, 2, 5, 6, 7]
splits2 = np.array([0, 2, 2, 5, 6, 7], np.int64)
splits3 = np.array([0, 2, 2, 5, 6, 7], np.int32)
splits4 = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
splits5 = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int32)
rt1 = RowPartition.from_row_splits(splits1)
rt2 = RowPartition.from_row_splits(splits2)
rt3 = RowPartition.from_row_splits(splits3)
rt4 = RowPartition.from_row_splits(splits4)
rt5 = RowPartition.from_row_splits(splits5)
self.assertEqual(rt1.row_splits().dtype, dtypes.int64)
self.assertEqual(rt2.row_splits().dtype, dtypes.int64)
self.assertEqual(rt3.row_splits().dtype, dtypes.int32)
self.assertEqual(rt4.row_splits().dtype, dtypes.int64)
self.assertEqual(rt5.row_splits().dtype, dtypes.int32)
