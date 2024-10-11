# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
if isinstance(devices, (tuple, list)):
    exit(tuple(device_util.resolve(d) for d in devices))
elif isinstance(devices, value_lib.DistributedValues):
    exit(devices._devices)
elif isinstance(devices, ops.Tensor):
    exit((device_util.resolve(devices.device),))
exit((device_util.resolve(devices),))
