# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
lhs = np.array([[2.0, 3.0], [4.0, 5.0]], dtype=dtype)
rhs = np.array([[10.0], [20.0]], dtype=dtype)
ops.Dot(ops.Constant(c, lhs), ops.Constant(c, rhs))
self._ExecuteAndCompareClose(c, expected=[np.dot(lhs, rhs)])
