# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.SliceInDim(
    ops.Constant(c, NumpyArrayS32([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
    start_index=1,
    limit_index=2,
    stride=1,
    dimno=1)
self._ExecuteAndCompareExact(c, expected=[[[2], [5], [8]]])
ops.SliceInDim(
    ops.Constant(c, NumpyArrayS32([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
    start_index=0,
    limit_index=3,
    stride=2,
    dimno=0)
self._ExecuteAndCompareExact(c, expected=[[[1, 2, 3], [7, 8, 9]]])
