# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
"""Computation (dtype, dtype) -> dtype that adds its two parameters."""
c = self._NewComputation("add_param0_by_param1")
shape = xla_client.shape_from_pyval(np.array(0, dtype=dtype))
shape = shape.with_major_to_minor_layout_if_absent()
ops.Add(ops.Parameter(c, 0, shape), ops.Parameter(c, 1, shape))
exit(c.build())
