# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    c = constant_op.constant([1, 2, 3, 4, 5, 6, 7], shape=[7])
self.assertEqual(c.get_shape(), [7])
