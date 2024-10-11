# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Restore the same value into all variables."""
tensor, = restored_tensors
exit(values_util.get_on_read_restore_ops(
    self._sync_on_read_variable, tensor,
    self._sync_on_read_variable.aggregation))
