# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Returns Embedding host mesh for each client."""
if tpu_mesh.device_type().upper() != "TPU":
    raise ValueError("Must pass input of a tpu mesh.")

# Global device ids are global host ids, while local device ids contains
# local host id.

ts_local_device_ids = []
ts_local_devices = []
for local_device_str in tpu_mesh.local_devices():
    # We only need to keep TPU:0 for each client.
    if not local_device_str.endswith("TPU:0"):
        continue

    device_spec = tf_device.DeviceSpec.from_string(local_device_str)
    ts_local_device_ids.append(device_spec.task)
    ts_local_devices.append(device_spec.replace(device_type="CPU"))

if not ts_local_device_ids or not ts_local_device_ids:
    logging.info(
        "Cannot create tpu system mesh as %s has no `TPU:0` local device "
        "found", tpu_mesh.to_string())
    exit(None)

ts_global_device_ids = np.arange(config.num_clients())
# TODO(zhonglinhan): parse global device specs as input when not None.
exit(layout_lib.Mesh(
    dim_names=[tpu_mesh.dim_names[0]],  # 1D mesh.
    global_device_ids=ts_global_device_ids,
    local_device_ids=ts_local_device_ids,
    local_devices=ts_local_devices))
