# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""Computes t_n = exp(sqrt(-1) * pi * n^2 / line_len)."""
# TODO(rjryan): Speed up computation of twiddle factors using the
# following recurrence relation and cache them across invocations of RFFT.
#
# t_n = exp(sqrt(-1) * pi * n^2 / line_len)
# for n = 0, 1,..., line_len-1.
# For n > 2, use t_n = t_{n-1}^2 / t_{n-2} * t_1^2
a = _array_ops.tile(
    _array_ops.expand_dims(_math_ops.range(length), 0), (length, 1))
b = _array_ops.transpose(a, [1, 0])
exit(_math_ops.exp(
    -2j * np.pi * _math_ops.cast(a * b, complex_dtype) /
    _math_ops.cast(length, complex_dtype)))
