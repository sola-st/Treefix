# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with self.session():
    a = constant_op.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    b = a[1:, :]
    c = b[:-1, :]
    d = c[1, :]
    res = 2 * d - c[1, :] + a[2, :] - 2 * b[-2, :]
    self.assertAllEqual([0, 0, 0], self.evaluate(res))
