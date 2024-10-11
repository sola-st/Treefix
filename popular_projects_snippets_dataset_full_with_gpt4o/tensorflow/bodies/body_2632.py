# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform == "tpu":
    self.skipTest("TPU doesn't support 64bit tanh")
c = self._NewComputation()
arr = NumpyArrayF64([-0.2, 3.3, 12.1, 0.1, 0.0001])
ops.Tanh(ops.Constant(c, arr))
self._ExecuteAndCompareClose(c, expected=[np.tanh(arr)], rtol=1e-12)
