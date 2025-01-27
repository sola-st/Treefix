# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
z = array_ops.zeros((1, 2, 3))
self.assertAllEqual(z.get_shape().as_list(), [1, 2, 3])

m1 = array_ops.slice(z, [0, 0, 0], [-1, -1, -1])
self.assertAllEqual(m1.get_shape().as_list(), [1, 2, 3])

m2 = array_ops.slice(z, [0, 0, 0], [constant_op.constant(1) + 0, 2, -1])
self.assertAllEqual(m2.get_shape().as_list(), [1, 2, 3])
