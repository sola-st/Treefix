# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Builds a Topology object.

    If `serialized` is not `None`, the topology is parsed from `serialized` and
    the other arguments are ignored. Otherwise, the topology is computed from
    `mesh_shape` and `device_coordinates`.

    Args:
      serialized: A serialized `TopologyProto`, or `None`. If not `None`, the
        serialized proto is parsed to discover the topology.
      mesh_shape: A sequence of 4 positive integers, or `None`. If not `None`,
        the shape of the TPU topology, in number of cores. Ignored if
        `serialized` is not `None`.
      device_coordinates: A rank 3 numpy array that describes the mapping from
        TensorFlow TPU devices to TPU fabric coordinates, or `None`. If
        specified, array is a rank 3 int32 array with shape
        `[tasks, devices, axis]`.  `tasks` is the number of tasks in the TPU
        cluster, `devices` is the number of TPU devices per task, and `axis` is
        the number of axes in the TPU cluster topology. Each entry gives the
        `axis`-th coordinate in the topology of a task/device pair. TPU
        topologies are 4-dimensional, with dimensions `(x, y, z, core number)`.
        This arg is ignored if `serialized is not `None`.

    Raises:
      ValueError: If `serialized` does not describe a well-formed topology.
      ValueError: If `serialized` is `None` and `mesh_shape` is not a sequence
        of 4 positive integers.
      ValueError: If `serialized` is `None` and `device_coordinates` is not a
        rank 3 numpy int32 array that describes a valid coordinate mapping.
    """

self._serialized = serialized

if serialized:
    self._parse_topology(serialized)
else:
    self._mesh_shape = np.asarray(mesh_shape, dtype=np.int32)
    self._device_coordinates = np.asarray(device_coordinates, np.int32)
    if len(self._mesh_shape) != 4 or any(self._mesh_shape < 1):
        raise ValueError("`mesh_shape` must be a sequence of 4 positive "
                         f"entries; got `mesh_shape={self._mesh_shape}`")

    if (len(self._device_coordinates.shape) != 3 or
        self._device_coordinates.shape[2] != len(self._mesh_shape)):
        raise ValueError(
            "`device_coordinates` must be a rank 3 int32 array "
            "with minor dimension equal to the `mesh_shape` rank"
            "got device_coordinates.shape={} len(device_coordinates.shape)={} device_coordinates.shape[2]={} mesh_shape={}, len(mesh_shape)={}"
            .format(self._device_coordinates.shape,
                    len(self._device_coordinates.shape),
                    self._device_coordinates.shape[2], self._mesh_shape,
                    len(self._mesh_shape)))

self._topology_tasks, self._topology_devices = self._invert_topology()

# Coordinates of devices that are missing
self._missing_devices = np.argwhere(self._topology_tasks < 0)
