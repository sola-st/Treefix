# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
indices = [
    constant_op.constant([0, 4, 7]),
    constant_op.constant([1, 6]),
    constant_op.constant([2, 3, 5]),
    array_ops.zeros([0], dtype=dtypes.int32)
]
data = [
    constant_op.constant([[0, 1], [40, 41], [70, 71]]),
    constant_op.constant([[10, 11], [60, 61]]),
    constant_op.constant([[20, 21], [30, 31], [50, 51]]),
    array_ops.zeros([0, 2], dtype=dtypes.int32)
]
stitched_t = self.stitch_op(indices, data)
stitched_val = self.evaluate(stitched_t)
self.assertAllEqual([[0, 1], [10, 11], [20, 21], [30, 31], [40, 41],
                     [50, 51], [60, 61], [70, 71]], stitched_val)
# Dimension 0 is max(flatten(indices))+1.
self.assertEqual([8, 2], stitched_t.get_shape().as_list())
