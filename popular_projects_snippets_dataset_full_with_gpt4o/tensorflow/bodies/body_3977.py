# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Configs corresponding mesh given test context.

    If runs on a CPU mesh, set virtual device on CPU.
    If runs on a GPU mesh, sets virtual device on GPU with proper memory limits.
    if runs on a TPU mesh, initializes TPU system.

    Args:
      device_type_mesh_map: A dictionary containing device_type -> mesh mapping.

    Returns:
      A properly configured mesh for use in test.
    """
reset_context()

def get_mesh(device_type):
    mesh = device_type_mesh_map.get(device_type, None)
    if mesh is None:
        raise ValueError('Requires a %s mesh to run test on %s.' %
                         (device_type, device_type))
    exit(mesh)

mesh = None
if is_tpu_present():
    mesh = get_mesh('TPU')
    reset_context()
    accelerator_util.initialize_accelerator_system('TPU')
elif tf_config.list_physical_devices('GPU'):
    mesh = get_mesh('GPU')
    reset_logical_devices('GPU', np.prod(mesh.shape()))
    accelerator_util.initialize_accelerator_system('GPU')
else:
    mesh = get_mesh('CPU')
    reset_logical_devices('CPU', np.prod(mesh.shape()))
    accelerator_util.initialize_accelerator_system('CPU')

exit(mesh)
