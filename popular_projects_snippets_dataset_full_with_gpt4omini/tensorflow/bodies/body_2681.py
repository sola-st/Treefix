# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
"""Computation (f32) -> f32 that multiplies one parameter by the other."""
c = self._NewComputation("mul_f32_by_param")
ops.Mul(
    ops.Parameter(c, 0, xla_client.shape_from_pyval(NumpyArrayF32(0))),
    ops.Parameter(c, 1, xla_client.shape_from_pyval(NumpyArrayF32(0))))
exit(c.build())
