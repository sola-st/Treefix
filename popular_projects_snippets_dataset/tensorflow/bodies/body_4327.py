# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/mesh_util.py
"""Creates a single-client mesh.

  If both `mesh_dims` and `devices` are specified, they must match each otehr.
  As a special case, when all arguments are missing, this creates a 1D CPU mesh
  with an empty name, assigning all available devices to that dimension.

  Args:
    mesh_dims: A list of (dim_name, dim_size) tuples. Defaults to a single
      batch-parallel dimension called 'x' using all devices. As a special case,
      a single-element mesh_dims whose dim_size is -1 also uses all devices.
    mesh_name: Name of the created mesh. Defaults to ''.
    devices: String representations of devices to use. This is the device part
      of tf.DeviceSpec, e.g. 'CPU:0'. Defaults to all available logical devices.
    device_type: If `devices` is missing, the type of devices to use. Defaults
      to 'CPU'.
    use_xla_spmd: Boolean when True, will use XLA SPMD instead of
      DTensor SPMD.

  Returns:
    A single-client mesh created from specified or default arguments.
  """
device_specs, device_type = _make_device_specs(devices, device_type)

local_spec = tf_device.DeviceSpec(job=config.job_name(), replica=0, task=0)
device_specs = [local_spec.make_merged_spec(d) for d in device_specs]

if mesh_dims is None:
    mesh_dims = [('x', len(device_specs))]
elif len(mesh_dims) == 1 and mesh_dims[0][1] == -1:
    # Replace -1 dim_size in a 1D mesh will the number of all devices.
    mesh_dims[0] = (mesh_dims[0][0], len(device_specs))

dim_names = [d[0] for d in mesh_dims]
shape = [d[1] for d in mesh_dims]

if np.prod(shape) != len(device_specs):
    raise ValueError(f'length of devices ({len(device_specs)}) must be '
                     f'equal to total size of the mesh of shape {shape}')

global_device_ids = np.arange(len(device_specs)).reshape(shape)
local_device_ids = np.ravel(global_device_ids).tolist()
mesh = layout.Mesh(
    dim_names=dim_names,
    global_device_ids=global_device_ids,
    local_device_ids=local_device_ids,
    local_devices=device_specs,
    mesh_name=mesh_name,
    use_xla_spmd=use_xla_spmd)
_print_context(
    num_global_devices=len(device_specs),
    num_clients=1,
    client_id=0,
    device_type=device_type,
    mesh=mesh)
exit(mesh)
