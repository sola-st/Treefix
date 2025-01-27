# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_matmul_op_test.py
if callable(a):
    a = a()
if callable(b):
    b = b()
with self.assertRaisesRegex(exc, message):
    self.evaluate(ragged_math_ops.matmul(a, b, **kwargs))
