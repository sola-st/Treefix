# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
_ = ops.ReplicaId(c)
self._ExecuteAndCompareExact(c, expected=[0])
