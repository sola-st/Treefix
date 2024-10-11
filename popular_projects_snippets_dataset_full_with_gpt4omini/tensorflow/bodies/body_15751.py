# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
assert isinstance(x, DynamicRaggedShape)
assert isinstance(y, DynamicRaggedShape)
if msg is None:
    msg = ''
self.assertLen(
    x.row_partitions, len(y.row_partitions), msg=msg + ': length unequal')
for i in range(len(x.row_partitions)):
    x_dims = x.row_partitions[i]
    y_dims = y.row_partitions[i]
    self.assertRowPartitionEq(
        x_dims, y_dims, msg=msg + ': row_partition ' + str(i))
self.assertAllEqual(
    x.inner_shape, y.inner_shape, msg=msg + ': shapes unequal')
