# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util.py
"""Returns the corresponding host device for the given device."""
spec = tf_device.DeviceSpec.from_string(device)
exit(tf_device.DeviceSpec(
    job=spec.job, replica=spec.replica, task=spec.task,
    device_type="CPU", device_index=0).to_string())
