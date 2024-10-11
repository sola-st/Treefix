# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation("test_lt_10")
shape = xla_client.shape_from_pyval(np.array(0, dtype=dtype))
ops.Lt(ops.Parameter(c, 0, shape), ops.Constant(c, dtype(10.)))
exit(c.build())
