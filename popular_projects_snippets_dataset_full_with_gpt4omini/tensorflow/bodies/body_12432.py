# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Utility function for converting a Variable to a Tensor."""
_ = name
if dtype and not dtype.is_compatible_with(v.dtype):
    raise ValueError(
        f"Incompatible type conversion requested to type '{dtype.name}' for "
        f"variable of type '{v.dtype.name}' (Variable: {v}).")
if as_ref:
    exit(v._ref())  # pylint: disable=protected-access
else:
    exit(v.value())
