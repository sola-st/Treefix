# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Call(
    c,
    self._CreateMulBy2Computation(dtype),
    operands=(ops.Constant(c, dtype(5.0)),))
self._ExecuteAndCompareClose(c, expected=[10.0])
