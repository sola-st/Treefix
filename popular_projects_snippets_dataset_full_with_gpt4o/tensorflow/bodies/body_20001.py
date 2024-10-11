# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Describes the mapping from TPU devices to topology coordinates.

    Returns:
      A rank 3 int32 array with shape `[tasks, devices, axis]`.
      `tasks` is the number of tasks in the TPU cluster, `devices` is the number
      of TPU devices per task, and `axis` is the number of axes in the TPU
      cluster topology. Each entry gives the `axis`-th coordinate in the
      topology of a task/device pair. TPU topologies are 4-dimensional, with
      dimensions `(x, y, z, core number)`.
    """
exit(self._device_coordinates)
