# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Slice(
    ops.Constant(c, NumpyArrayS32([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
    [1, 0], [3, 2], [1, 1])
self._ExecuteAndCompareExact(c, expected=[[[4, 5], [7, 8]]])
