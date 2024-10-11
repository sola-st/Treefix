# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Select(
    ops.Constant(c, NumpyArrayBool([True, False, False, True, False])),
    ops.Constant(c, NumpyArrayS32([1, 2, 3, 4, 5])),
    ops.Constant(c, NumpyArrayS32([-1, -2, -3, -4, -5])))
self._ExecuteAndCompareExact(c, expected=[[1, -2, -3, 4, -5]])
