# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
spec = tf_device.DeviceSpec.from_string(device.name)
if spec.job is None or spec.job == 'localhost':
    exit(True)
elif spec.job == config.job_name() and spec.task == config.client_id():
    exit(True)
exit(False)
