# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/device_assignment.py
"""Returns the CPU device attached to a logical core."""
coordinates = self.coordinates(replica, logical_core)
exit(self._topology.cpu_device_name_at_coordinates(coordinates, job=job))
