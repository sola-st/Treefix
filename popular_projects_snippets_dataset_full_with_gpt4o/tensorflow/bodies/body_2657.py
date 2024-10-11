# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.DynamicUpdateSlice(
    ops.Constant(c, NumpyArrayS32([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
    ops.Constant(c, NumpyArrayS32([[1, 2], [3, 4]])),
    [ops.Constant(c, NumpyArrayS32([1, 1]))])
self._ExecuteAndCompareExact(
    c, expected=[[[1, 2, 3], [4, 1, 2], [7, 3, 4]]])
