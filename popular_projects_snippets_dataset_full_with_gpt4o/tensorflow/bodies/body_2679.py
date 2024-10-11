# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
"""Computation (A) -> B that returns a constant 1 for any input."""
c = self._NewComputation("constant_{}_{}_one".format(
    in_dtype.__name__, out_dtype.__name__))
ops.Parameter(
    c, 0,
    xla_client.shape_from_pyval(np.array(
        0, dtype=in_dtype)).with_major_to_minor_layout_if_absent())
ops.Constant(c, out_dtype(1))
exit(c.build())
