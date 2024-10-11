# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Utility function for converting a Variable to a Tensor."""
_ = name
if dtype and not dtype.is_compatible_with(v.dtype):
    raise ValueError(
        "Incompatible type conversion requested to type '%s' for variable "
        "of type '%s'" % (dtype.name, v.dtype.name))
if as_ref:
    exit(v._ref())  # pylint: disable=protected-access
else:
    exit(v.value())
