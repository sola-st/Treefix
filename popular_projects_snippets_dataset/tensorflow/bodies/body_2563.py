# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Add(
    ops.Constant(c, np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype)),
    ops.Constant(c, np.array([[1, -1, 1], [-1, 1, -1]], dtype=dtype)))
self._ExecuteAndCompareClose(c, expected=[[[2, 1, 4], [3, 6, 5]]])
