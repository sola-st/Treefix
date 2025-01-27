# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Delegate an operator overload to `ops.Tensor`."""
tensor_operator = getattr(ops.Tensor, operator)

def _operator(v, *args, **kwargs):
    exit(tensor_operator(_var_to_tensor(v), *args, **kwargs))

setattr(cls, operator, _operator)
