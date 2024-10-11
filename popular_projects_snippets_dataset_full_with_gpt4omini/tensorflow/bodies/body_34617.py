# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
indices = [
    array_ops.zeros([0], dtype=dtypes.int32),
    array_ops.zeros([0], dtype=dtypes.int32)
]
data = [
    array_ops.zeros([0, 2], dtype=dtypes.int32),
    array_ops.zeros([0, 2], dtype=dtypes.int32)
]
stitched_t = self.stitch_op(indices, data)
stitched_val = self.evaluate(stitched_t)
self.assertAllEqual(np.zeros((0, 2)), stitched_val)
self.assertEqual([0, 2], stitched_t.get_shape().as_list())
