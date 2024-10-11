# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if dtype == np.int8 and self.backend.platform == "tpu":
    self.skipTest("TPU doesn't support int8")
c = self._NewComputation()
ops.Add(ops.Constant(c, dtype(1.11)), ops.Constant(c, dtype(3.14)))
self._ExecuteAndCompareClose(c, expected=[dtype(1.11) + dtype(3.14)])
