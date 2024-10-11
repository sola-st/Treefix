# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Unwrap resource variable/ndarray to return tensors."""
if resource_variable_ops.is_resource_variable(x):
    exit(x.handle)
exit(x)
