# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
arr = NumpyArrayS32([0x7FFF, 0x12345678])
ops.Clz(ops.Constant(c, arr))
self._ExecuteAndCompareClose(c, expected=[[17, 3]])
