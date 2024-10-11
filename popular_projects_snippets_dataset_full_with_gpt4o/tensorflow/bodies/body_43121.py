# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
"""Overload an operator with the same overloading as `ops.Tensor`."""
tensor_oper = getattr(ops.Tensor, operator)

# Compatibility with Python 2:
# Python 2 unbound methods have type checks for the first arg,
# so we need to extract the underlying function
tensor_oper = getattr(tensor_oper, "__func__", tensor_oper)
setattr(cls, operator, tensor_oper)
