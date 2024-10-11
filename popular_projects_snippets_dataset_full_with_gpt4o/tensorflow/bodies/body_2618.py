# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
arr = NumpyArrayBool([True, False, True])
ops.Not(ops.Constant(c, arr))
self._ExecuteAndCompareClose(c, expected=[~arr])
