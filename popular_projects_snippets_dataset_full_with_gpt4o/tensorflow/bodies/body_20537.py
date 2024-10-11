# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_system_metadata.py
spec = tf_device.DeviceSpec.from_string(device.name)
exit((spec.job, spec.replica, spec.task, spec.device_type,
        spec.device_index))
