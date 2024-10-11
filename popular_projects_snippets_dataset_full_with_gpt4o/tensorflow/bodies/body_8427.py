# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if self._device_assignment is None:
    exit(self._tpu_metadata.num_cores)
exit(self._device_assignment.num_replicas)
