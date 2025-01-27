# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/device_assignment.py
"""Constructs a `DeviceAssignment` object.

    Args:
      topology: A `Topology` object that describes the physical TPU topology.
      core_assignment: A logical to physical core mapping, represented as a
        rank 3 numpy array. See the description of the `core_assignment`
        property for more details.

    Raises:
      ValueError: If `topology` is not `Topology` object.
      ValueError: If `core_assignment` is not a rank 3 numpy array.
    """
if not isinstance(topology, Topology):
    raise ValueError("topology must be a Topology object, got {}".format(
        type(topology)))
core_assignment = np.asarray(core_assignment, dtype=np.int32)

self._topology = topology

if core_assignment.ndim != 3:
    raise ValueError("core_assignment must be a rank 3 numpy array, "
                     f"got shape {core_assignment.shape}")

self._num_replicas = core_assignment.shape[0]
self._num_cores_per_replica = core_assignment.shape[1]

if core_assignment.shape[-1] != topology.mesh_rank:
    raise ValueError(
        "core_assignment.shape[-1] must have size equal to topology "
        f"rank ({topology.mesh_rank}), got "
        f"core_assignment.shape={core_assignment.shape}")

self._core_assignment = core_assignment
self._task_and_cores_to_replicas = _compute_task_and_cores_to_replicas(
    self._core_assignment, topology)
