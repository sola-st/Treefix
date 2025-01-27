# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
value_rowids = constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
nrows = constant_op.constant(5, dtypes.int64)

with self.assertRaisesRegex(ValueError, r'Expected nrows >= 0; got -2'):
    RowPartition.from_value_rowids(
        value_rowids=array_ops.placeholder_with_default(value_rowids, None),
        nrows=-2)

with self.assertRaisesRegex(
    ValueError, r'Expected nrows >= value_rowids\[-1\] \+ 1; got nrows=2, '
    r'value_rowids\[-1\]=4'):
    RowPartition.from_value_rowids(value_rowids=value_rowids, nrows=2)

with self.assertRaisesRegex(
    ValueError, r'Expected nrows >= value_rowids\[-1\] \+ 1; got nrows=4, '
    r'value_rowids\[-1\]=4'):
    RowPartition.from_value_rowids(value_rowids=value_rowids, nrows=4)

with self.assertRaisesRegex(ValueError, r'Shape \(7, 1\) must have rank 1'):
    RowPartition.from_value_rowids(
        value_rowids=array_ops.expand_dims(value_rowids, 1), nrows=nrows)

with self.assertRaisesRegex(ValueError, r'Shape \(1,\) must have rank 0'):
    RowPartition.from_value_rowids(
        value_rowids=value_rowids, nrows=array_ops.expand_dims(nrows, 0))
