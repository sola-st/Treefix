# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
arr = NumpyArrayF32([3.3, 12.1])
ops.Ceil(ops.Constant(c, arr))
self._ExecuteAndCompareClose(c, expected=[np.ceil(arr)])
