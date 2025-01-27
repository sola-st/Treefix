# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
"""Computation (dtype, dtype) -> bool that tests param0 >= param1."""
c = self._NewComputation("param0_lt_param1")
shape = xla_client.shape_from_pyval(np.array(0, dtype=dtype))
shape = shape.with_major_to_minor_layout_if_absent()
ops.Ge(ops.Parameter(c, 0, shape), ops.Parameter(c, 1, shape))
exit(c.build())
