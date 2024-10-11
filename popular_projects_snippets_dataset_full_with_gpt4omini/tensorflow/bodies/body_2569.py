# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Add(
    ops.Mul(
        ops.Constant(c, dtype(2)),
        ops.Constant(c, np.array([2.2, 3.3, 4.4, 5.5], dtype=dtype))),
    ops.Constant(c, np.array([100, -100, 200, -200], dtype)))
self._ExecuteAndCompareClose(
    c, expected=[[104.4, -93.4, 208.8, -189]], rtol=2e-3)
