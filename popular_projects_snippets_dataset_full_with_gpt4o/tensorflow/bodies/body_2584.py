# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Add(
    ops.Parameter(c, 0, xla_client.shape_from_pyval(NumpyArrayF32(0.))),
    ops.Constant(c, np.float32(3.14)))
self._ExecuteAndCompareClose(
    c, arguments=[NumpyArrayF32(1.11)], expected=[4.25])
