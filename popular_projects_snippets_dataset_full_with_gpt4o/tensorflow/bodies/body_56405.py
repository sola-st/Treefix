# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
gpus = config.list_physical_devices('GPU')
self.assertNotEqual(len(gpus), 0)

if len(gpus) > 1:
    # Assert if other GPUs were not configured
    config.set_memory_growth(gpus[0], True)
    with self.assertRaisesRegex(ValueError, 'cannot differ'):
        c = context.context().config

    # If we limit visibility to GPU 0, growth is fine
    config.set_visible_devices(gpus[0], 'GPU')
    c = context.context().config
    self.assertTrue(c.gpu_options.allow_growth)

    # Default setting for second GPU is False and works if we set visibility
    config.set_visible_devices(gpus[1], 'GPU')
    c = context.context().config
    self.assertFalse(c.gpu_options.allow_growth)

    # Growth now fails because all the GPUs are visible and not the same
    config.set_visible_devices(gpus, 'GPU')
    with self.assertRaisesRegex(ValueError, 'cannot differ'):
        c = context.context().config

for gpu in gpus:
    config.set_memory_growth(gpu, True)

c = context.context().config
self.assertTrue(c.gpu_options.allow_growth)

with self.assertRaisesRegex(ValueError, 'memory limit'):
    config.set_logical_device_configuration(gpus[-1], [
        context.LogicalDeviceConfiguration(),
        context.LogicalDeviceConfiguration()
    ])

self.assertIsNone(config.get_logical_device_configuration(gpus[-1]))
config.set_logical_device_configuration(gpus[-1], [
    context.LogicalDeviceConfiguration(memory_limit=10),
    context.LogicalDeviceConfiguration(memory_limit=10)
])

c = context.context().config
self.assertFalse(c.gpu_options.allow_growth)

with self.assertRaisesRegex(ValueError, 'virtual devices'):
    config.set_memory_growth(gpus[-1], False)
