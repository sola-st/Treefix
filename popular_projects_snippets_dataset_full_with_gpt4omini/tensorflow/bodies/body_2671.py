# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
a = np.array([[4, 6, 8, 10], [6, 45, 54, 63], [8, 54, 146, 166],
              [10, 63, 166, 310]],
             dtype=np.float32)
c = self._NewComputation()
ops.Tuple(c, ops.SVD(ops.Constant(c, a)))
u, d, v = self._Execute(c, ())
self.assertLess(np.linalg.norm(a - np.matmul(u * d, v.T)), 1e-3)
