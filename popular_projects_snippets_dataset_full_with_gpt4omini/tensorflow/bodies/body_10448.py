# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Divides `x / y` assuming `x, y >= 0`, treating `0 / 0 = 0`."""
exit(x // math_ops.maximum(y, 1))
