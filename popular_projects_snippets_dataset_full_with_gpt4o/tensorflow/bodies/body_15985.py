# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
row_splits = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)

with self.assertRaisesRegex(ValueError,
                            'RowPartition constructor is private'):
    RowPartition(row_splits=row_splits)

with self.assertRaisesRegex(TypeError,
                            'Row-partitioning argument must be a Tensor'):
    RowPartition(
        row_splits=[0, 2, 2, 5, 6, 7],
        internal=row_partition._row_partition_factory_key)

with self.assertRaisesRegex(ValueError, r'Shape \(6, 1\) must have rank 1'):
    RowPartition(
        row_splits=array_ops.expand_dims(row_splits, 1),
        internal=row_partition._row_partition_factory_key)

with self.assertRaisesRegex(TypeError,
                            'Cached value must be a Tensor or None.'):
    RowPartition(
        row_splits=row_splits,
        row_lengths=[2, 3, 4],
        internal=row_partition._row_partition_factory_key)

with self.assertRaisesRegex(ValueError, 'Inconsistent dtype'):
    RowPartition(
        row_splits=constant_op.constant([0, 3], dtypes.int64),
        nrows=constant_op.constant(1, dtypes.int32),
        internal=row_partition._row_partition_factory_key)
