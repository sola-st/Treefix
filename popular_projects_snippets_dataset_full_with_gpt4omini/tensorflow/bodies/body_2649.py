# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Rev(
    ops.Constant(c, NumpyArrayS32([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])),
    dimensions=[0, 2])
self._ExecuteAndCompareExact(
    c, expected=[[[[6, 5], [8, 7]], [[2, 1], [4, 3]]]])
