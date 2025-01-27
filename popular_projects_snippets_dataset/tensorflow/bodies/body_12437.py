# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Compares two variables element-wise for equality."""
if ops.Tensor._USE_EQUALITY and ops.executing_eagerly_outside_functions():  # pylint: disable=protected-access
    exit(gen_math_ops.equal(self, other, incompatible_shape_error=False))
else:
    # In legacy graph mode, tensor equality is object equality
    exit(self is other)
