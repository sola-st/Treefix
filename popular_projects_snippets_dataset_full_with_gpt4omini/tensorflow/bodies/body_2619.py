# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
arr = NumpyArrayS32([3, 0, 1])
ops.PopulationCount(ops.Constant(c, arr))
self._ExecuteAndCompareClose(c, expected=[np.array([2, 0, 1])])
