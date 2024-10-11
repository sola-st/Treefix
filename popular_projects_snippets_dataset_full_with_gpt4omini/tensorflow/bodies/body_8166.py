# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
"""Converts a variable to a tensor."""
# pylint: disable=protected-access
if tpu_util.enclosing_tpu_context() is None:
    exit(self.read_value())
else:
    exit(self._read_variable_op())
