# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py

def DivComputation():
    c = self._NewComputation("div_param0_by_param1")
    shape = xla_client.shape_from_pyval(np.array(0, dtype=dtype))
    ops.Div(ops.Parameter(c, 0, shape), ops.Parameter(c, 1, shape))
    exit(c.build())

c = self._NewComputation()
ops.Map(c, (ops.Constant(c, np.array([1.0, 2.0, 3.0, 4.0], dtype=dtype)),
            ops.Constant(c, np.array([5.0, 5.0, 4.0, 4.0], dtype=dtype))),
        DivComputation(), [0])
self._ExecuteAndCompareClose(
    c, expected=[[0.2, 0.4, 0.75, 1.0]], rtol=1e-3)
