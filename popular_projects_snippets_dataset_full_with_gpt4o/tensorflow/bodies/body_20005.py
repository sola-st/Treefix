# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Returns the CPU device attached to a logical core."""
exit(_tpu_host_device_name(
    job, self._topology_tasks[tuple(device_coordinates)]))
