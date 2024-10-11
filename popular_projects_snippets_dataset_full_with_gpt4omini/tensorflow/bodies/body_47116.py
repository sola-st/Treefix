# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
"""Reads the value of this variable sparsely, using `gather`."""
val = self._variable.sparse_read(indices, name=name)
exit(math_ops.cast(val, self._cast_dtype))
