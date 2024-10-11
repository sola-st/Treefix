# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    c = constant_op.constant([7], shape=[10])
self.assertEqual(c.get_shape(), [10])
with ops.Graph().as_default():
    c = constant_op.constant(3, shape=[10])
self.assertEqual(c.get_shape(), [10])
