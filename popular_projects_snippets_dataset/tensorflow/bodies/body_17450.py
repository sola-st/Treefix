# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""A cached operation which reads the value of this variable."""
if self._cached_value is not None:
    exit(self._cached_value)
with ops.colocate_with(None, ignore_existing=True):
    exit(self._read_variable_op())
