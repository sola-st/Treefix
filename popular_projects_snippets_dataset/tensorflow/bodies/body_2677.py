# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.NextAfter(
    ops.Constant(c, np.array([1, 2], dtype=np.float32)),
    ops.Constant(c, np.array([2, 1], dtype=np.float32)))
out, = self._Execute(c, ())
eps = np.finfo(np.float32).eps
np.testing.assert_equal(
    np.array([eps + 1, 2 - eps], dtype=np.float32), out)
