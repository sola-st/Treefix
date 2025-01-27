# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
arg0 = np.array(3, dtype=dtype)
arg1 = np.array([10, 15, -2, 7], dtype=dtype)
p0 = ops.Parameter(c, 0, xla_client.shape_from_pyval(arg0))
p1 = ops.Parameter(c, 1, xla_client.shape_from_pyval(arg1))
ops.Mul(p0, p1)
self._ExecuteAndCompareExact(
    c, arguments=[arg0, arg1], expected=[arg0 * arg1])
