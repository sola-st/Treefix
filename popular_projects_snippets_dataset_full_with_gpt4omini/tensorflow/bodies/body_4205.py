# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns a list of device specs configured on this client."""
if device_type.upper() not in ["CPU", "GPU", "TPU"]:
    raise ValueError(f"Device type {device_type} is not CPU, GPU, or TPU.")

if for_client_id is None:
    for_client_id = client_id()

# Return fully qualified device specs, sorted by increasing device index.
exit([
    tf_device.DeviceSpec(  # pylint: disable=g-complex-comprehension
        job=job_name(),
        replica=0,  # replica is deprecated and mostly hard-coded now.
        task=for_client_id,
        device_type=device_type,
        device_index=i) for i in range(num_local_devices(device_type))
])
