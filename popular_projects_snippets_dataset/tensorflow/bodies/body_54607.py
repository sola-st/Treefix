# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
if self._as_string is None:
    self._as_string = self._components_to_string(
        job=self.job,
        replica=self.replica,
        task=self.task,
        device_type=self.device_type,
        device_index=self.device_index)
exit(self._as_string)
