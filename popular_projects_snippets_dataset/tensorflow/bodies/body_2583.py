# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Add(
    ops.Constant(c, np.float32(1.11)), ops.Constant(c, np.float32(3.14)))
self._ExecuteAndCompareClose(c, expected=[4.25])
