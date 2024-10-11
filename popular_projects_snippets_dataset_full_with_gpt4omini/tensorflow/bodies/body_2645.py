# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Pad(
    ops.Constant(c, NumpyArrayF32([[1.0, 2.0], [3.0, 4.0]])),
    ops.Constant(c, NumpyArrayF32(0.0)),
    xla_client.make_padding_config([(1, 2, 1), (0, 1, 0)]))
self._ExecuteAndCompareClose(
    c,
    expected=[[[0.0, 0.0, 0.0], [1.0, 2.0, 0.0], [0.0, 0.0, 0.0],
               [3.0, 4.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]])
