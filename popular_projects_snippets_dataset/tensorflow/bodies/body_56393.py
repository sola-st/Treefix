# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
config.set_soft_device_placement(False)
gpus = config.list_physical_devices('GPU')
self.assertNotEqual(len(gpus), 0)

self.assertIsNone(config.get_logical_device_configuration(gpus[-1]))
config.set_logical_device_configuration(gpus[-1], [
    context.LogicalDeviceConfiguration(memory_limit=10),
    context.LogicalDeviceConfiguration(memory_limit=10)
])
self.assertEqual(len(config.get_logical_device_configuration(gpus[-1])), 2)

logical_gpus = config.list_logical_devices('GPU')
self.assertTrue(len(logical_gpus), len(gpus) + 1)
for i in range(0, len(logical_gpus)):
    with ops.device('/device:GPU:' + str(i)):
        a = array_ops.identity(1.0)
        self.evaluate(a)

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Could not satisfy'):
    with ops.device('/device:GPU:' + str(len(logical_gpus))):
        a = array_ops.identity(1.0)
        self.evaluate(a)

    # Modifying the GPU configuration is not supported
with self.assertRaisesRegex(RuntimeError, 'cannot be modified'):
    config.set_logical_device_configuration(gpus[-1], [
        context.LogicalDeviceConfiguration(memory_limit=20),
        context.LogicalDeviceConfiguration(memory_limit=20)
    ])

with self.assertRaisesRegex(RuntimeError, 'cannot be modified'):
    config.set_logical_device_configuration(gpus[-1], [
        context.LogicalDeviceConfiguration(memory_limit=10),
        context.LogicalDeviceConfiguration(memory_limit=10),
        context.LogicalDeviceConfiguration(memory_limit=10)
    ])

# Setting the same GPU configuration is fine
config.set_logical_device_configuration(gpus[-1], [
    context.LogicalDeviceConfiguration(memory_limit=10),
    context.LogicalDeviceConfiguration(memory_limit=10)
])
