# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    c = constant_op.constant(1)
self.assertEqual(c.get_shape(), [])
