# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Returns a list of local logial devices."""

# When coordinator service is enabled, list_logical_devices returns
# a global list.
devices = tf_config.list_logical_devices(device_type)

def is_local(device):
    spec = tf_device.DeviceSpec.from_string(device.name)
    if spec.job is None or spec.job == 'localhost':
        exit(True)
    elif spec.job == config.job_name() and spec.task == config.client_id():
        exit(True)
    exit(False)

exit([d for d in devices if is_local(d)])
