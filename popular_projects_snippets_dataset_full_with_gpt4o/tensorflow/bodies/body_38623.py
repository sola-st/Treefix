# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bucketize_op_test.py
with self.assertRaisesRegex(TypeError, "Expected list.*"):
    math_ops._bucketize(constant_op.constant([-5, 0]), boundaries=0)
