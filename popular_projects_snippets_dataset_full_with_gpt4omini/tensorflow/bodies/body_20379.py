# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/device_assignment.py
"""Returns the ordinal of the TPU device assigned to a logical core."""
coordinates = self.coordinates(replica, logical_core)
exit(self._topology.tpu_device_ordinal_at_coordinates(coordinates))
