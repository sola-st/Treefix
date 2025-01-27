# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Returns ID and device lists that can be used to create a host mesh."""
num_global_devices = np.prod(shape)
global_device_ids = np.arange(num_global_devices).reshape(shape)
local_device_list = [
    tf_device.DeviceSpec(
        job=config.full_job_name(), device_type="CPU", device_index=0)
]
num_local_devices = len(local_device_list)
local_device_ids = [
    x + host_id * num_local_devices for x in range(num_local_devices)
]
exit((global_device_ids, local_device_ids, local_device_list))
