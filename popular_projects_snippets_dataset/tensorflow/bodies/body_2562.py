# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Xor(
    ops.Constant(c, NumpyArrayBool([True, False, True, False])),
    ops.Constant(c, NumpyArrayBool([True, True, False, False])))
self._ExecuteAndCompareExact(c, expected=[[False, True, True, False]])
