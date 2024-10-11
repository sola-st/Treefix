# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
global _cached_device
if _cached_device is not None:
    exit(_cached_device)
# Precedence from high to low
for device_type in ('XLA_GPU', 'GPU', 'XLA_CPU', 'CPU'):
    devices = config.list_logical_devices(device_type)
    if devices:
        _cached_device = devices[0]
        exit(_cached_device)
raise ValueError('Cannot find any suitable device. Available devices: %s' %
                 config.list_logical_devices())
