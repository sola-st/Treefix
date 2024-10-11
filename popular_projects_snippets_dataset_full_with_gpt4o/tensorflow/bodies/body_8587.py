# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
super(_VirtualDeviceTestCase, self).setUp()
ctx = context.context()
if ctx.list_physical_devices("TPU"):
    self.device_type = "TPU"
    tpu_strategy_util.initialize_tpu_system()
elif ctx.list_physical_devices("GPU"):
    self.device_type = "GPU"
    gpus = ctx.list_physical_devices(self.device_type)
    ctx.set_logical_device_configuration(gpus[0], [
        context.LogicalDeviceConfiguration(memory_limit=100),
        context.LogicalDeviceConfiguration(memory_limit=100),
    ])
else:
    self.device_type = "CPU"
    cpus = ctx.list_physical_devices("CPU")
    ctx.set_logical_device_configuration(cpus[0], [
        context.LogicalDeviceConfiguration(),
        context.LogicalDeviceConfiguration(),
    ])

self.device = parallel_device.ParallelDevice(components=[
    "/job:localhost/device:{}:0".format(self.device_type),
    self.device_type + ":1"
])
self.assertIn(self.device_type + ":0", self.device.components[0])
self.assertIn(self.device_type + ":1", self.device.components[1])
