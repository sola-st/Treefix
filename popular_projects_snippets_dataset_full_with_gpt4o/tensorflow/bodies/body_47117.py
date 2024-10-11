# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
"""Gather slices of the variable into a Tensor."""
val = self._variable.gather_nd(indices, name=name)
exit(math_ops.cast(val, self._cast_dtype))
