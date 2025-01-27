# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
row_partitions = [
    RowPartition.from_value_rowids([0, 2, 4], nrows=5),
    RowPartition.from_value_rowids([0, 1, 2], nrows=3)
]
inner_shape = [3]
rts = DynamicRaggedShape(row_partitions, inner_shape, validate=True,
                         static_inner_shape=[3])
static_inner_shape = tensor_util.constant_value(rts.inner_shape)
static_valid_rowids0 = tensor_util.constant_value(
    rts.row_partitions[0].value_rowids())
static_valid_rowids1 = tensor_util.constant_value(
    rts.row_partitions[1].value_rowids())
self.assertAllEqual(static_inner_shape, [3])
self.assertAllEqual(static_valid_rowids0, [0, 2, 4])
self.assertAllEqual(static_valid_rowids1, [0, 1, 2])
