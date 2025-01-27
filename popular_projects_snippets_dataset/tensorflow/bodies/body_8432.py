# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
exit(tuple(self._tpu_devices[:, self._logical_device_stack[-1]]))
