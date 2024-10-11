# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Eq(
    ops.Constant(c, NumpyArrayS32([1, 2, 3, 4])),
    ops.Constant(c, NumpyArrayS32([4, 2, 3, 1])))
self._ExecuteAndCompareExact(c, expected=[[False, True, True, False]])
