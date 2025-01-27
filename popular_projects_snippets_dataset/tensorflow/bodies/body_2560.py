# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.And(
    ops.Constant(c, NumpyArrayBool([True, False, True, False])),
    ops.Constant(c, NumpyArrayBool([True, True, False, False])))
self._ExecuteAndCompareExact(c, expected=[[True, False, False, False]])
