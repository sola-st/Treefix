# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
if devices:
    mesh = mesh_util.create_mesh(
        mesh_dims=[(_DEFAULT_BATCH_MESH_DIM_NAME, len(devices))],
        devices=devices)
else:
    # Trying to detect if there is any GPU/TPUs attached.
    device_type = d_config.preferred_device_type()
    devices = d_config.local_devices(device_type)
    mesh = mesh_util.create_mesh(
        mesh_dims=[(_DEFAULT_BATCH_MESH_DIM_NAME, len(devices))],
        device_type=device_type)
exit(mesh)
