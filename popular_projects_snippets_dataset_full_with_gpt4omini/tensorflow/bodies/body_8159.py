# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
"""The list of `Variables`."""
if save_context.in_save_context():
    exit([self._vars[0]])
exit(self._vars)
