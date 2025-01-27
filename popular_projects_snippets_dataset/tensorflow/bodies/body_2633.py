# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Transpose(ops.Constant(c, array), permutation)
expected = np.transpose(array, permutation)
self._ExecuteAndCompareClose(c, expected=[expected])
