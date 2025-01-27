# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
with test_util.use_gpu():
    indices = [constant_op.constant(0), constant_op.constant(1)]
    data = [constant_op.constant(40.0), constant_op.constant(60.0)]
    for step in -1, 1:
        stitched_t = data_flow_ops.dynamic_stitch(indices[::step], data)
        stitched_val = self.evaluate(stitched_t)
        self.assertAllEqual([40.0, 60.0][::step], stitched_val)
        # Dimension 0 is max(flatten(indices))+1.
        self.assertEqual([2], stitched_t.get_shape().as_list())
