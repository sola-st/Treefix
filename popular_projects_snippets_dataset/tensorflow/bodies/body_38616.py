# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
with self.cached_session():
    with self.assertRaisesOpError(err):
        self.evaluate(array_ops.transpose(x, p))
