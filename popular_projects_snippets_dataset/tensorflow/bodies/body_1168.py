# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
data = np.array([[4., -1., 2.], [-1., 6., 0], [2., 0., 5.]])
for dtype in self.float_types:
    self._verifyCholesky(data.astype(dtype))
