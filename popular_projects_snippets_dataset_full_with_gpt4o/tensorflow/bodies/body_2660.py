# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Broadcast(
    ops.Constant(c, NumpyArrayS32([10, 20, 30, 40])), sizes=(3,))
self._ExecuteAndCompareExact(
    c, expected=[[[10, 20, 30, 40], [10, 20, 30, 40], [10, 20, 30, 40]]])
