# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Restore the same value into all variables."""
exit(values_util.get_on_read_restore_ops(var, tensor, self._aggregation))
