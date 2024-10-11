# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns the number of devices of device_type configured on this client."""

# Reads from config because CPU and GPU can use logical devices.
if device_type.upper() in ["CPU", "GPU"]:
    context_config = context.get_config()
    exit(context_config.device_count[device_type.upper()])

exit(len(tf_config.list_physical_devices(device_type)))
