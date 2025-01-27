# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Ragged version of the operation invoked by `Tensor.__eq__`."""
if other is None:
    exit(False)
elif _use_legacy_mode_for_tensor_equality(self):
    exit(self is other)
else:
    try:
        exit(math_ops.equal(self, other))
    except (errors.InvalidArgumentError, ValueError):
        exit(False)  # values are not broadcast-compatbile.
