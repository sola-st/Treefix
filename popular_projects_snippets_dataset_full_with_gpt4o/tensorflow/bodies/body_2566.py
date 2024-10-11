# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.ShiftRightLogical(
    ops.Constant(c, NumpyArrayS32([-1])),
    ops.Constant(c, NumpyArrayS32([1])))
self._ExecuteAndCompareClose(c, expected=[[2**31 - 1]])
