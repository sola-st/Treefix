# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
cpus = config.list_physical_devices('CPU')
self.assertEqual(len(cpus), 1)

config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])

context.ensure_initialized()

vcpus = config.list_logical_devices('CPU')
self.assertEqual(len(vcpus), 2)

with ops.device('/device:CPU:0'):
    a = constant_op.constant(1.0)
    self.evaluate(a)
with ops.device('/device:CPU:1'):
    b = constant_op.constant(1.0)
    self.evaluate(b)
with ops.device('/device:CPU:2'):
    c = constant_op.constant(1.0)
    self.evaluate(c)
if test_util.is_gpu_available():
    self.assertIn('GPU:0', c.device)
else:
    self.assertIn('CPU:0', c.device)

# Ensure we can place ops on each of the device names
for vcpu in vcpus:
    with ops.device(vcpu.name):
        d = constant_op.constant(1.0)
        self.evaluate(d)

    # Modifying the CPU configuration is not supported
with self.assertRaisesRegex(RuntimeError, 'cannot be modified'):
    config.set_logical_device_configuration(cpus[0], [
        context.LogicalDeviceConfiguration(),
        context.LogicalDeviceConfiguration(),
        context.LogicalDeviceConfiguration()
    ])

# Setting the same CPU configuration is fine
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])
