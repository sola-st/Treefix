# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    t = constant_op.constant(10.0)
    x = ops.convert_to_tensor(t)
self.assertIs(t, x)
