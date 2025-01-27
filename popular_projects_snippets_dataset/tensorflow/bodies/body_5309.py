# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Restore the same value into all variables."""
tensor, = restored_tensors
exit(values_util.get_on_write_restore_ops(self._mirrored_variable, tensor))
