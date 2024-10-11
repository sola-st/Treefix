# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation("div_param0_by_param1")
shape = xla_client.shape_from_pyval(np.array(0, dtype=dtype))
ops.Div(ops.Parameter(c, 0, shape), ops.Parameter(c, 1, shape))
exit(c.build())
