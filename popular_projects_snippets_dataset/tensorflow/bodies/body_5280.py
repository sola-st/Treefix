# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.value())
if self._policy:
    exit(self._policy.value(self))
exit(self._get_on_device_or_primary().value())
