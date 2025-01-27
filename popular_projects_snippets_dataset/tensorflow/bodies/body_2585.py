# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Add(
    ops.Parameter(c, 0, xla_client.shape_from_pyval(NumpyArrayF32(0.))),
    ops.Parameter(c, 1, xla_client.shape_from_pyval(NumpyArrayF32(0.))))
self._ExecuteAndCompareClose(
    c,
    arguments=[NumpyArrayF32(1.11),
               NumpyArrayF32(3.14)],
    expected=[4.25])
