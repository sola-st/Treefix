# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
arr = NumpyArrayF32([-0.2, 3.3, 12.1, 0.1, 0.0001])
ops.Tan(ops.Constant(c, arr))
self._ExecuteAndCompareClose(c, expected=[np.tan(arr)])
