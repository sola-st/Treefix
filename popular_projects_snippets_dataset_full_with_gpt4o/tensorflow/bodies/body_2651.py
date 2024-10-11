# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Clamp(
    ops.Constant(c, NumpyArrayF32(-1)),
    ops.Constant(c, NumpyArrayF32([-2, -1, 0, 1, 2, 3])),
    ops.Constant(c, NumpyArrayF32(2)))
self._ExecuteAndCompareExact(c, expected=[[-1, -1, 0, 1, 2, 2]])
