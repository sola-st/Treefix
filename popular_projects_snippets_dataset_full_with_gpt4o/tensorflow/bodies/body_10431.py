# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""A sequence of [1+0j, -1+0j, 1+0j, -1+0j, ...] with length `length`."""
exit(_math_ops.cast(1 - 2 * (_math_ops.range(length) % 2),
                      complex_dtype))
