# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
# Use explicit numbering and pass parameter_num first. Sub is used since
# it's not commutative and can help catch parameter reversal within the
# computation.
c = self._NewComputation()
arg0 = np.array(2.0, dtype=dtype)
arg1 = np.array([-2.3, 3.3, -4.3, 5.3], dtype=dtype)
p1 = ops.Parameter(c, 1, xla_client.shape_from_pyval(arg1))
p0 = ops.Parameter(c, 0, xla_client.shape_from_pyval(arg0))
ops.Sub(p1, p0)
self._ExecuteAndCompareClose(
    c, arguments=[arg0, arg1], expected=[arg1 - arg0])
