# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Filters out objects with no direct variable dependencies for assertions."""
exit([o for o in full_list if o._gather_saveables_for_checkpoint()])  # pylint: disable=protected-access
