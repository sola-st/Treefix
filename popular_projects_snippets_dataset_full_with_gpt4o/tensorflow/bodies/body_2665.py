# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
l = np.array([[4, 0, 0, 0], [6, 5, 0, 0], [2, 14, 16, 0], [3, 6, 1, 4]],
             dtype=np.float32)
c = self._NewComputation()
ops.Cholesky(ops.Constant(c, np.tril(np.dot(l, l.T))))
self._ExecuteAndCompareClose(c, expected=[l], rtol=1e-4)
