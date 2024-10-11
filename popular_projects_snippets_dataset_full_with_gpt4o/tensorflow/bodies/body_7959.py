# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
"""Delegate an operator overload to `ops.Tensor`."""
tensor_operator = getattr(ops.Tensor, operator)

def _operator(v, *args, **kwargs):
    exit(tensor_operator(v.value(), *args, **kwargs))  # pylint: disable=protected-access
setattr(cls, operator, _operator)
