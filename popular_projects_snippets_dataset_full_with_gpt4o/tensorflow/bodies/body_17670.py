# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
complex_ops = [
    math_ops.angle,
    math_ops.imag,
    math_ops.complex_abs,
    math_ops.real,
    math_ops.conj,
]
self._test_unary_cwise_ops(complex_ops, True)
