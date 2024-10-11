# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
row_splits = [0, 2, 5, 6, 6, 7]
rp = RowPartition.from_row_splits(row_splits, validate=False)
if context.executing_eagerly():
    expected_repr = 'tf.RowPartition(row_splits=[0 2 5 6 6 7])'
else:
    expected_repr = ('tf.RowPartition(row_splits='
                     'Tensor("RowPartitionFromRowSplits/row_splits:0", '
                     'shape=(6,), dtype=int64))')
self.assertEqual(repr(rp), expected_repr)
self.assertEqual(str(rp), expected_repr)
