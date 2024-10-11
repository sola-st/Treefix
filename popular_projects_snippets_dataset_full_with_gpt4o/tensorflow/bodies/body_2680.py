# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
"""Computation (dtype) -> dtype that multiplies its parameter by 2."""
c = self._NewComputation("mul_f32_by2")
ops.Mul(
    ops.Parameter(
        c, 0,
        xla_client.shape_from_pyval(np.array(
            0, dtype=dtype)).with_major_to_minor_layout_if_absent()),
    ops.Constant(c, dtype(2.0)))
exit(c.build())
