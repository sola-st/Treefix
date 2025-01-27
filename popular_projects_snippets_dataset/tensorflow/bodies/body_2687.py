# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if dtype == np.float64 and self.backend.platform == "tpu":
    self.skipTest("TPU doesn't support float64")
c = self._NewComputation()
ops.Map(c, [ops.Constant(c, np.array([1.0, 2.0, 3.0, 4.0], dtype=dtype))],
        self._CreateMulBy2Computation(dtype), [0])
self._ExecuteAndCompareClose(c, expected=[[2.0, 4.0, 6.0, 8.0]])
