# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
dtypes = [np.float16, np.float32, np.float64, np.int32, np.int64]
data = [-1, 0, 1]
for t in dtypes:
    for x in data:
        for y in data:
            with self.subTest(t=t, x=x, y=y):
                self.assertEqual(self._compareScalar(math_ops.less, x, y, t), x < y)
                self.assertEqual(
                    self._compareScalar(math_ops.less_equal, x, y, t), x <= y)
                self.assertEqual(
                    self._compareScalar(math_ops.greater, x, y, t), x > y)
                self.assertEqual(
                    self._compareScalar(math_ops.greater_equal, x, y, t), x >= y)
                self.assertEqual(
                    self._compareScalar(math_ops.equal, x, y, t), x == y)
                self.assertEqual(
                    self._compareScalar(math_ops.not_equal, x, y, t), x != y)
data = [-1, 0, 1, -1j, 1j, 1 + 1j, 1 - 1j]
for t in [np.complex64, np.complex128]:
    for x in data:
        for y in data:
            with self.subTest(t=t, x=x, y=y):
                self.assertEqual(
                    self._compareScalar(math_ops.equal, x, y, t), x == y)
                self.assertEqual(
                    self._compareScalar(math_ops.not_equal, x, y, t), x != y)
