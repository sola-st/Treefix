# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Div(
    ops.Constant(c, np.array([1.5, 2.5, 3.0, -10.8], dtype=dtype)),
    ops.Constant(c, dtype(2.0)))
self._ExecuteAndCompareClose(
    c, expected=[[0.75, 1.25, 1.5, -5.4]], rtol=2e-3)
