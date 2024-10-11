# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# nrows is not known at graph creation time.
value_rowids = constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
value_rowids = array_ops.placeholder_with_default(value_rowids, shape=None)

rp = RowPartition.from_value_rowids(value_rowids, validate=False)

rp_value_rowids = rp.value_rowids()
rp_nrows = rp.nrows()

self.assertIs(rp_value_rowids, value_rowids)  # value_rowids
self.assertAllEqual(rp_value_rowids, value_rowids)
self.assertAllEqual(rp_nrows, 5)
