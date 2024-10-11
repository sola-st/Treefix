# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Iota(c, xla_client.PrimitiveType.F32, 10)
self._ExecuteAndCompareExact(
    c, expected=[np.arange(10, dtype=np.float32)])
