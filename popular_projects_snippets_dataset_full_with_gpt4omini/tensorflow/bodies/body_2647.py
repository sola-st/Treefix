# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Reshape(
    ops.Constant(c, NumpyArrayS32([[1, 2], [3, 4], [5, 6]])),
    dimensions=[0, 1],
    new_sizes=[2, 3])
self._ExecuteAndCompareExact(c, expected=[[[1, 2, 3], [4, 5, 6]]])
