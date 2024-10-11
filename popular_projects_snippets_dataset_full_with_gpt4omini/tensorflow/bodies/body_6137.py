# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
# Currently we only support equal number of devices on each worker.
exit(self._group_size / len(self._devices))
