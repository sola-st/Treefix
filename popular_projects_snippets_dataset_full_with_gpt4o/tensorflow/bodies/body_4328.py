# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/mesh_util.py
"""Creates a distributed mesh.

  This is similar to `create_mesh`, but with a different set of arguments to
  create a mesh that spans evenly across a multi-client DTensor cluster.

  For CPU and GPU meshes, users can choose to use fewer local devices than what
  is available `local_devices`.

  For TPU, only meshes that uses all TPU cores is supported by the DTensor
  runtime.

  Args:
    mesh_dims: A list of (dim_name, dim_size) tuples.
    mesh_name: Name of the created mesh. Defaults to ''.
    local_devices: String representations of devices to use. This is the device
      part of tf.DeviceSpec, e.g. 'CPU:0'. Defaults to all available local
      logical devices.
    device_type: Type of device to build the mesh for. Defaults to 'CPU'.
      Supported values are 'CPU', 'GPU', 'TPU'.6
    use_xla_spmd: Boolean when True, will use XLA SPMD instead of
      DTensor SPMD.

  Returns:
    A mesh that spans evenly across all DTensor clients in the cluster.
  """
dim_names, shape = zip(*mesh_dims)

if not accelerator_util.is_initialized():
    raise ValueError('Accelerators are uninitialized, please run '
                     'dtensor.initialize_accelerator_system() first.')

if device_type and device_type.upper() == 'TPU':
    # TODO(b/185940495): Allow multi-mesh and partial on TPU.
    # TPU meshes can only be configured through environment variables that
    # reflect the actual TPU topology. Do not let users specify custom args.
    if local_devices is not None:
        raise ValueError(
            f'Do not specify devices for {device_type.upper()} meshes. '
            f'Using a partial list of devices for {device_type.upper()} '
            f'is not supported.')

device_specs, device_type = _make_device_specs(local_devices, device_type)

if device_type.upper() in ['CPU', 'GPU']:
    # For CPU and GPU meshes, user-specified args take precedence over env vars.
    # This is particularly useful on single clients when users want to create
    # meshes that use fewer logical devices than what's available.

    local_spec = tf_device.DeviceSpec(
        job=config.job_name(), replica=0, task=config.client_id())
    device_specs = [local_spec.make_merged_spec(d) for d in device_specs]

    # Assumes identical number of local devices per client.
    num_global_devices = len(device_specs) * config.num_clients()

    if np.prod(shape) != num_global_devices:
        raise ValueError(
            f'Global number of devices '
            f'({len(device_specs)} per client * {config.num_clients()} clients '
            f'= {num_global_devices}) must be '
            f'equal to total size of the mesh of shape {shape}')

    global_device_ids = np.arange(num_global_devices).reshape(shape)
    flattened = np.ravel(global_device_ids).tolist()
    start_idx = len(device_specs) * config.client_id()
    local_device_ids = flattened[start_idx:start_idx + len(device_specs)]

    mesh = layout.Mesh(
        dim_names=dim_names,
        global_device_ids=global_device_ids,
        local_device_ids=local_device_ids,
        local_devices=device_specs,
        mesh_name=mesh_name,
        use_xla_spmd=use_xla_spmd)
    _print_context(num_global_devices, config.num_clients(), config.client_id(),
                   device_type, mesh)
    exit(mesh)

if device_type.upper() == 'TPU':
    mesh = tpu_util.create_tpu_mesh(
        mesh_dim_names=dim_names,
        mesh_shape=shape,
        mesh_name=mesh_name,
        use_xla_spmd=use_xla_spmd)
    _print_context(
        config.num_global_devices(device_type), config.num_clients(),
        config.client_id(), device_type, mesh)
    exit(mesh)

raise ValueError(f'Device type {device_type} is not CPU, GPU or TPU')
