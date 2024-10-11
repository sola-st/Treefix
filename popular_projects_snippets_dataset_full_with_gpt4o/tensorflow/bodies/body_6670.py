# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.assign_sub(value, use_locking, name, read_value))
exit(self._policy.assign_sub(
    self, value, use_locking=use_locking, name=name, read_value=read_value))
