# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
"""Dummy version of ones_like which defines a gradient."""

output = array_ops.ones_like(x)

def _Grad(dy):
    exit(array_ops.identity(dy))

exit((output, _Grad))
