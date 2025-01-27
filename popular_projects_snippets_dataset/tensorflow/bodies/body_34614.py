# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
indices = [constant_op.constant([1, 6, 2, 3, 5, 0, 4, 7])]
data = [constant_op.constant([10, 60, 20, 30, 50, 0, 40, 70])]
stitched_t = self.stitch_op(indices, data)
stitched_val = self.evaluate(stitched_t)
self.assertAllEqual([0, 10, 20, 30, 40, 50, 60, 70], stitched_val)
# Dimension 0 is max(flatten(indices))+1.
self.assertEqual([8], stitched_t.get_shape().as_list())
