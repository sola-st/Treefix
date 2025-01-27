# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/device_assignment.py
"""Computes a device_assignment of a computation across a TPU topology.

  Attempts to choose a compact grid of cores for locality.

  Returns a `DeviceAssignment` that describes the cores in the topology assigned
  to each core of each replica.

  `computation_shape` and `computation_stride` values should be powers of 2 for
  optimal packing.

  Args:
    topology: A `Topology` object that describes the TPU cluster topology. To
      obtain a TPU topology, evaluate the `Tensor` returned by
      `initialize_system` using `Session.run`. Either a serialized
      `TopologyProto` or a `Topology` object may be passed. Note: you must
        evaluate the `Tensor` first; you cannot pass an unevaluated `Tensor`
        here.
    computation_shape: A rank 1 int32 numpy array with size equal to the
      topology rank, describing the shape of the computation's block of cores.
      If None, the `computation_shape` is `[1] * topology_rank`.
    computation_stride: A rank 1 int32 numpy array of size `topology_rank`,
      describing the inter-core spacing of the `computation_shape` cores in the
      TPU topology. If None, the `computation_stride` is `[1] * topology_rank`.
    num_replicas: The number of computation replicas to run. The replicas will
      be packed into the free spaces of the topology.
    device_order_mode: An enum of `DeviceOrderMode` class which indicates
      whether to assign devices to form rings or meshes, or let the library to
      choose.

  Returns:
    A DeviceAssignment object, which describes the mapping between the logical
    cores in each computation replica and the physical cores in the TPU
    topology.

  Raises:
    ValueError: If `topology` is not a valid `Topology` object.
    ValueError: If `computation_shape` or `computation_stride` are not 1D int32
      numpy arrays with shape [3] where all values are positive.
    ValueError: If computation's replicas cannot fit into the TPU topology.
  """
# Deserialize the Topology proto, if it is a string.
if isinstance(topology, bytes):
    topology = Topology(serialized=topology)

if not isinstance(topology, Topology):
    raise ValueError(
        f"`topology` is not a Topology object; got {type(topology)}")

topology_rank = len(topology.mesh_shape)
mesh_shape = topology.mesh_shape
if computation_shape is None:
    computation_shape = np.array([1] * topology_rank, dtype=np.int32)
else:
    computation_shape = np.asarray(computation_shape, dtype=np.int32)

if computation_stride is None:
    computation_stride = np.array([1] * topology_rank, dtype=np.int32)
else:
    computation_stride = np.asarray(computation_stride, dtype=np.int32)

if computation_shape.shape != (topology_rank,):
    raise ValueError(
        f"computation_shape must have shape [{topology_rank}]; "
        f"got {computation_shape.shape}"
    )
if computation_stride.shape != (topology_rank,):
    raise ValueError(
        f"computation_stride must have shape [{topology_rank}]; "
        f"got {computation_stride.shape}"
    )

if any(computation_shape < 1):
    raise ValueError(
        "computation_shape must be positive; got computation_shape={}".format(
            computation_shape))
if any(computation_stride < 1):
    raise ValueError(
        "computation_stride must be positive; got computation_stride={}".format(
            computation_stride))

# Computes the physical size of one computation instance.
computation_footprint = computation_shape * computation_stride
if any(computation_footprint > mesh_shape):
    raise ValueError(
        "computation footprint {} does not fit in TPU topology shape {}".format(
            computation_footprint, mesh_shape))

# Computes how many copies of the computation footprint fit in the mesh.
block_counts = mesh_shape // computation_footprint

replica_counts = block_counts * computation_stride
max_replicas = np.prod(replica_counts)
if num_replicas > max_replicas:
    raise ValueError(
        "requested {} replicas but only {} replicas with shape {} and "
        "computation_stride {} fit in a TPU mesh of shape {}".format(
            num_replicas, max_replicas, computation_shape, computation_stride,
            mesh_shape))

def ceil_of_ratio(n, m):
    exit((n + m - 1) // m)

if topology.missing_devices.size == 0:
    replica_shape = [0] * topology_rank
    if num_replicas > 0:
        remaining_replicas = num_replicas
        remaining_dims = topology_rank

        # Choose dimensions as close to an equal cube as possible,
        # in order of increasing dimension size. By visiting dimensions
        # in increasing size, we assign the most constrained dimension
        # first, so we won't make infeasible choices.
        #
        # As a secondary sort order, visit the last dimension (core index) first,
        # then the other dimensions in increasing order. This means we try to use
        # both cores on the same chip in preference to two cores on different
        # chips.  We visit the x dimension first, and the z dimension last, so
        # that we prefer to arrange adjacent replicas on the same machine when
        # possible.
        #
        # For example, if num_replicas == 4, we prefer to use a replica_shape of
        # (2,1,1,2) over (1,1,2,2).

        for x, ni in sorted(((x, ((i + 1) % topology_rank))
                             for (i, x) in enumerate(replica_counts))):
            i = (ni + topology_rank - 1) % topology_rank
            target_size = int(math.ceil(remaining_replicas**(1.0 / remaining_dims)))
            replica_shape[i] = min(target_size, x)
            remaining_replicas = ceil_of_ratio(remaining_replicas, replica_shape[i])
            remaining_dims -= 1

        assert remaining_replicas == 1 and remaining_dims == 0

    # Assigns an offset to each replica such that no two replicas overlap.
    replica_offsets = np.full([num_replicas, topology_rank], -1, dtype=np.int32)

    enable_3d_tiling = (
        topology_rank == 4 and
        computation_shape[-1] == mesh_shape[-1]  # Only handle 3D case.
        and np.prod(computation_stride) == 1  # Ensure no stride.
        and num_replicas == max_replicas)  # Full replication.

    if device_order_mode != DeviceOrderMode.AUTO:
        if device_order_mode == DeviceOrderMode.RING and not enable_3d_tiling:
            raise ValueError(
                "device_order_mode=DeviceOrderMode.RING is not compatible with the "
                "3D tiling current topology.  Try setting "
                "device_order_mode=DeviceOrderMode.AUTO"
            )
        enable_3d_tiling = device_order_mode == DeviceOrderMode.RING

    if enable_3d_tiling:
        assignment = []
        inner_ring = _ring_3d(computation_shape[0], computation_shape[1],
                              computation_shape[2])
        outer_ring = _ring_3d(replica_shape[0], replica_shape[1],
                              replica_shape[2])

        for replica in range(num_replicas):
            outer_x, outer_y, outer_z = outer_ring[replica]
            per_replica_assignment = []
            for index in range(np.prod(computation_shape)):
                inner_x, inner_y, inner_z = inner_ring[index // mesh_shape[-1]]
                px = outer_x * computation_shape[0] + inner_x
                py = outer_y * computation_shape[1] + inner_y
                pz = outer_z * computation_shape[2] + inner_z
                pi = index % mesh_shape[-1]
                per_replica_assignment.append([px, py, pz, pi])
            assignment.append(per_replica_assignment)
    else:
        for replica in range(num_replicas):
            # Chooses a replica number in each axis.
            t = replica
            pos = []
            # Visit the core number first.
            for dim in np.concatenate([[replica_shape[-1]], replica_shape[:-1]]):
                pos.append(t % dim)
                t //= dim
            replica_pos = np.concatenate([pos[1:], [pos[0]]])

            # Determines where that replica starts in each axis.
            outer = replica_pos // computation_stride
            inner = replica_pos % computation_stride
            replica_offsets[replica, :] = outer * computation_footprint + inner

        # Computes a logical core -> physical core mapping for each replica.
        indices = [
            np.arange(0, computation_shape[i] * computation_stride[i],
                      computation_stride[i]) for i in range(topology_rank)
        ]
        indices = np.concatenate(
            [i[..., np.newaxis] for i in np.meshgrid(*indices, indexing="ij")],
            axis=-1)
        indices = indices.reshape((-1, topology_rank))
        assignment = indices + replica_offsets[:, np.newaxis, :]
else:
    # We have a slice with missing chips. We define a simple assignment by
    # ignoring computation stride. This assignment should enable a consistent
    # and correct device assignment on degraded slices. It is optimal when
    # weights are not sharded. But this device assignment may be sub-optimal for
    # other model parallelism scenarios.
    assert np.prod(computation_stride) == 1
    # Next, we check if we have sufficient devices.
    assert num_replicas * np.prod(
        computation_shape) <= topology.num_tasks * topology.num_tpus_per_task
    # Map replicas to physical devices in task order.
    device_coordinates = topology.device_coordinates
    assignment = []
    devices_per_replica = np.prod(computation_shape)
    for rindex in range(num_replicas):
        replica_assignment = []
        for index in range(devices_per_replica):
            logical_id = rindex * devices_per_replica + index
            # Pick logical cores in task order
            task = logical_id // topology.num_tpus_per_task
            device = logical_id % topology.num_tpus_per_task
            # Append physical cores to the replica assignment
            replica_assignment.append(device_coordinates[task, device, :])
        assignment.append(replica_assignment)

exit(DeviceAssignment(topology, core_assignment=assignment))
