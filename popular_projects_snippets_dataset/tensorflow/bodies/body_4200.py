# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Returns a distributed TPU mesh optimized for AllReduce ring reductions.

  Only as many as leading axes specified by `ring_axes` as necessary will be
  used to build rings, as long as the subslice formed by these axes have enough
  cores to contain a ring of the required size. The leftover axes in `ring_axes`
  won't affect results.

  This function always uses all TPU devices, and offers more customization than
  `tf.experimental.dtensor.create_distributed_mesh`.

  Args:
    mesh_dim_names: List of mesh dimension names.
    mesh_shape: Shape of the mesh.
    mesh_name: A unique name for the mesh. If empty, internally generate one.
    ring_dims: Optional; The number of leading (ring_dims > 0) or trailing
      (ring_dims < 0) mesh dimensions to build rings for. If unspecified, build
      rings for all but the first dimension.
    ring_axes: Optional; A permutation of ["x", "y", "z", "core"], specifying
      the order of TPU topology axes to build rings in. If unspecified, default
      to ["core", "x", "y", "z"].
    ring_bounds: Optional; The maximum number of devices on each axis, in the x,
      y, z, core order. If unspecified, default to physical topology limits.
    can_split_host_across_rings: Optional; If true, devices attached to the same
      host (i.e., DTensor client) may get assigned to different rings. Setting
      it to false may cause some combinations of arguments to be infeasible; see
      DeviceAssignmentTest.testCreateMesh[No]SplittingHosts* for examples.
    build_ring_across_rings: Optional; If true, also build a data-parallel ring
      across model-parallel rings. This ring could be strided.
    rotate_ring_across_rings: Optional; If true, build the data-parallel ring in
      column-major instead of row-major order.
    use_xla_spmd: Boolean when True, will use XLA SPMD instead of
      DTensor SPMD.
  """

logging.info("Building a TPU mesh %s of shape %s", mesh_name, mesh_shape)
logging.info("Requested ring_dims: %s", ring_dims)
logging.info("Requested ring_axes: %s", ring_axes)
logging.info("Requested ring_bounds: %s", ring_bounds)
logging.info("Requested can_split_host_across_rings: %s",
             can_split_host_across_rings)
if not mesh_name:
    mesh_name = "mesh_%f" % time.time()
logging.info("Requested mesh_name: %s", mesh_name)

# By default, build rings for all but the first (usually batch) dimension.
if ring_dims is None:
    ring_dims = 1 - len(mesh_shape)
elif ring_dims < -len(mesh_shape) or ring_dims > len(mesh_shape):
    raise ValueError("Invalid ring_dims value: %d" % ring_dims)
logging.info("Actual ring_dims: %s", ring_dims)

# By default, vary axes in the core -> x -> y -> z order.
if ring_axes is None:
    ring_axes = ["core", "x", "y", "z"]
elif len(ring_axes) != 4:
    raise ValueError("Expected 4 elements in ring_axes, got %s" % ring_axes)
elif sorted(ring_axes) != ["core", "x", "y", "z"]:
    raise ValueError("Invalid ring_axes value: %s" % ring_axes)
logging.info("Actual ring_axes: %s", ring_axes)

# Validate ring_bounds values.
if _tpu_topology is None:
    raise ValueError(
        "Invalid TPU topology, run dtensor.initialize_tpu_system() first")
topology_shape = list(_tpu_topology.mesh_shape)
if ring_bounds is None:
    ring_bounds = topology_shape
elif len(ring_bounds) != 4:
    raise ValueError("Expected 4 elements in ring_bounds, got %s" % ring_bounds)
elif ring_bounds > topology_shape:
    raise ValueError("ring_bounds %s should be <= topology sizes %s" %
                     (ring_bounds, topology_shape))
logging.info("Actual ring_bounds: %s", ring_bounds)

# Compute ring_size, the number of cores in a ring.
if ring_dims > 0:
    ring_size = np.prod(mesh_shape[:ring_dims])
elif ring_dims < 0:
    ring_size = np.prod(mesh_shape[ring_dims:])
else:
    ring_size = 1  # single-core rings
logging.info("Actual ring_size: %d", ring_size)

# Rearrange all cores according to the axis iteration order.
global_core_locations = _enumerate_core_locations(
    topology_shape, ring_bounds, ring_axes, can_split_host_across_rings,
    ring_size)
logging.vlog(1, "Enumerated core locations: %s", global_core_locations)
num_cores = len(global_core_locations)

# The mesh to be created must use all TPU cores in the system.
mesh_size = np.prod(mesh_shape)
if mesh_size != num_cores:
    raise ValueError(
        "Invalid mesh size: mesh shape %s cannot 1:1 map to %d TPU cores" %
        (mesh_shape, num_cores))

# Build a ring for the `ring_size` dimension and, if required, a strided ring
# for the orthogonal dimension.
if build_ring_across_rings:
    global_core_locations = _build_orthogonal_rings(global_core_locations,
                                                    ring_size,
                                                    rotate_ring_across_rings)
else:
    permutation = _build_all_reduce_ring(global_core_locations[:ring_size])
    for r in range(0, num_cores, ring_size):
        global_core_locations[r:r + ring_size] = [
            global_core_locations[r + permutation[i]] for i in range(ring_size)
        ]
    logging.vlog(1, "Permutated core locations: %s", global_core_locations)

# For this point on, change from List[CoreLocation] to List[List[int]] for
# easier interaction with the C++ API.
global_core_locations = [l.to_list() for l in global_core_locations]
if _dtensor_device is None:
    raise ValueError("Invalid system device, "
                     "run dtensor.initialize_accelerator_system() first")
global_core_ids = _dtensor_device.tpu_core_locations_to_ids(
    global_core_locations)

# Store a per-mesh mapping in the runtime.
_dtensor_device.set_tpu_core_ids(mesh_name, global_core_ids)

# Create the mesh by manually specifying local_device_ids.
local_core_locations = _tpu_topology.device_coordinates[config.client_id()]
indexes = [
    global_core_locations.index(list(local_core_location))
    for local_core_location in local_core_locations
]
global_device_ids, local_device_ids, local_device_list = _create_device_array(
    mesh_shape, _TPU_DEVICE_TYPE, None, local_device_ids=indexes)
exit(layout_lib.Mesh(mesh_dim_names, global_device_ids, local_device_ids,
                       local_device_list, mesh_name, use_xla_spmd))
