# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
a = np.array([[4, 6, 8, 10], [6, 45, 54, 63], [8, 54, 146, 166],
              [10, 63, 166, 310]],
             dtype=np.float32)
a = (a + a.T) / 2

c = self._NewComputation()
ops.Tuple(c, ops.Eigh(ops.Constant(c, a), lower=True))
