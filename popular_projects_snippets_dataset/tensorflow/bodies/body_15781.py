# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
x = constant_op.constant([3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0])
rt1 = RaggedTensor._from_row_partition(
    x,
    RowPartition.from_row_splits(row_splits=[0, 4, 7, 8],
                                 dtype=dtypes.int64, validate=False))
rt2 = rt1 * [[10], [100], [1000]]
self.assertAllClose(rt2.flat_values,
                    [30.0, 10.0, 40.0, 10.0, 100.0, 0.0, 200.0, 1000.0])
