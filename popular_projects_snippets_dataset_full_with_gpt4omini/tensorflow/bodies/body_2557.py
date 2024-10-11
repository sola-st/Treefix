# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Pow(
    ops.Constant(c, np.array([1.5, 2.5, 3.0], dtype=dtype)),
    ops.Constant(c, dtype(2.)))
self._ExecuteAndCompareClose(c, expected=[[2.25, 6.25, 9.]])
