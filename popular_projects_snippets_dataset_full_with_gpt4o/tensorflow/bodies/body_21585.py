# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
"""Restore the same value into both variables."""
tensor, = restored_tensors
exit(control_flow_ops.group(
    self._primary_variable.assign(tensor),
    self._mirrored_variable.assign(tensor)))
