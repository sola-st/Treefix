# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
arr = NumpyArrayF32([3.3, 12.1])
ops.Expm1(ops.Constant(c, arr))
self._ExecuteAndCompareClose(c, expected=[np.expm1(arr)])
