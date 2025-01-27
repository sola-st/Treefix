# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
row_splits = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
rp = RowPartition(
    row_splits=row_splits,
    internal=row_partition._row_partition_factory_key)
self.assertAllEqual(rp.row_splits(), [0, 2, 2, 5, 6, 7])
