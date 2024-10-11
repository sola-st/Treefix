# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Restore the same value into all variables."""
tensor, = restored_tensors
exit(self._distributed_variable._policy.get_restore_ops(  # pylint: disable=protected-access
    self._distributed_variable, tensor))
