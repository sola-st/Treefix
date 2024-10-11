# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm.py
"""Clips x to the range [-1., 1.]."""
exit(math_ops.maximum(math_ops.minimum(x, 1.), -1.))
