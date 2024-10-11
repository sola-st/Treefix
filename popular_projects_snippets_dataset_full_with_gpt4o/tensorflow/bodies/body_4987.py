# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
cpu_device = tf_device.DeviceSpec.from_string(device)
cpu_device = cpu_device.replace(device_type="CPU", device_index=0)
exit(cpu_device.to_string())
