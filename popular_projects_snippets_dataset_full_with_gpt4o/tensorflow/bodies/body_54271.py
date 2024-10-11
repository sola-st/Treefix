# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
values = constant_op.constant([2, 3, 5, 7], shape=[2, 2])
indices = constant_op.constant([0, 2])
x = math_ops.scalar_mul(-2, indexed_slices.IndexedSlices(values, indices))
self.assertAllEqual(x.values, [[-4, -6], [-10, -14]])
self.assertAllEqual(x.indices, [0, 2])
