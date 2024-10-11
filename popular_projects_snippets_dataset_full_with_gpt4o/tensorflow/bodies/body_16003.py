# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_uniform_row_length(5, nvals=10, nrows=2)
if context.executing_eagerly():
    expected_repr = ('tf.RowPartition(nrows=2, uniform_row_length=5)')
else:
    expected_repr = (
        'tf.RowPartition(nrows='
        'Tensor("RowPartitionFromUniformRowLength/'
        'nrows:0", shape=(), dtype=int64), '
        'uniform_row_length=Tensor("RowPartitionFromUniformRowLength/'
        'uniform_row_length:0", shape=(), dtype=int64))')
self.assertEqual(repr(rp), expected_repr)
self.assertEqual(str(rp), expected_repr)
