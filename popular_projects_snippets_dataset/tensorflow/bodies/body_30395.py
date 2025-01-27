# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
with self.assertRaisesOpError(err):
    self.evaluate(math_ops.cast(x, dtype))
