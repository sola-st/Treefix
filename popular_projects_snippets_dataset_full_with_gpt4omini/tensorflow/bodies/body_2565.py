# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.ShiftRightArithmetic(
    ops.Constant(c, NumpyArrayS32([-2])),
    ops.Constant(c, NumpyArrayS32([1])))
self._ExecuteAndCompareClose(c, expected=[[-1]])
