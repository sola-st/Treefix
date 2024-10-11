# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Returns the name of the TPU device assigned to a logical core."""
exit(_tpu_device_name(job,
                        self._topology_tasks[tuple(device_coordinates)],
                        self._topology_devices[tuple(device_coordinates)]))
