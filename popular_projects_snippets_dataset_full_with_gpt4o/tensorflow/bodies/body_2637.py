# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Gt(
    ops.Constant(c, NumpyArrayS32([1, 2, 3, 4, 9])),
    ops.Constant(c, NumpyArrayS32([1, 0, 2, 7, 12])))
self._ExecuteAndCompareExact(
    c, expected=[[False, True, True, False, False]])
