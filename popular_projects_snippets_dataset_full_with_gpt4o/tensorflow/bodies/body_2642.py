# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Max(
    ops.Constant(c, NumpyArrayF32([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
    ops.Constant(c, NumpyArrayF32([3, 4, 5])),
    broadcast_dimensions=(0,))
self._ExecuteAndCompareExact(
    c, expected=[[[3, 3, 3], [4, 5, 6], [7, 8, 9]]])
