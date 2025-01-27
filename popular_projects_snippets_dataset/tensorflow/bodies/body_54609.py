# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
"""Merge the properties of "dev" into this `DeviceSpec`.

    Note: Will be removed in TensorFlow 2.x since DeviceSpecs will become
          immutable.

    Args:
      dev: a `DeviceSpec`.
    """
(self.job, self.replica, self.task, self.device_type,
 self.device_index) = self._get_combined_properties(dev)
