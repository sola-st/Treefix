# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.assign(value, use_locking, name, read_value))
if self._policy:
    exit(self._policy.assign(
        self,
        value,
        use_locking=use_locking,
        name=name,
        read_value=read_value))
exit(values_util.on_write_assign(
    self, value, use_locking=use_locking, name=name, read_value=read_value))
