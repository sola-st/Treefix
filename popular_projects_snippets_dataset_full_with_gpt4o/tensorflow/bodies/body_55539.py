# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_vgpu_test.py
gpus = config.list_physical_devices('GPU')
if len(gpus) != 2:
    self.skipTest('Need 2 GPUs')

config.set_logical_device_configuration(gpus[0], [
    context.LogicalDeviceConfiguration(
        memory_limit=100, experimental_device_ordinal=0),
    context.LogicalDeviceConfiguration(
        memory_limit=100, experimental_device_ordinal=1)
])

config.set_logical_device_configuration(gpus[1], [
    context.LogicalDeviceConfiguration(
        memory_limit=100, experimental_device_ordinal=0),
    context.LogicalDeviceConfiguration(
        memory_limit=100, experimental_device_ordinal=1)
])

context.ensure_initialized()

vcpus = config.list_logical_devices('GPU')
self.assertEqual(len(vcpus), 4)
