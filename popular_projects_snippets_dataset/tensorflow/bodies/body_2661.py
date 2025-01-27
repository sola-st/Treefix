# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.BroadcastInDim(ops.Constant(c, NumpyArrayS32([1, 2])), [2, 2], [0])
self._ExecuteAndCompareExact(c, expected=[[[1, 1], [2, 2]]])
ops.BroadcastInDim(ops.Constant(c, NumpyArrayS32([1, 2])), [2, 2], [1])
self._ExecuteAndCompareExact(c, expected=[[[1, 2], [1, 2]]])
