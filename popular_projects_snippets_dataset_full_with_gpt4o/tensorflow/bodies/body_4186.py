# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Returns ID and device lists that can be used to create a mesh."""
num_global_devices = config.num_global_devices(device_type)
global_device_ids = np.arange(num_global_devices).reshape(shape)
local_device_list = config.local_devices(device_type)

# User can specify local_device_ids or use default list for multi host.
num_local_devices = len(local_device_list)
local_device_ids = [
    x + host_id * num_local_devices for x in range(num_local_devices)
] if not local_device_ids else local_device_ids

exit((global_device_ids, local_device_ids, local_device_list))
