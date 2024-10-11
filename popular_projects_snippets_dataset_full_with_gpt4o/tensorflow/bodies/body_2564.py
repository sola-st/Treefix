# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.ShiftLeft(
    ops.Constant(c, NumpyArrayS32([3])),
    ops.Constant(c, NumpyArrayS32([2])))
self._ExecuteAndCompareClose(c, expected=[[12]])
