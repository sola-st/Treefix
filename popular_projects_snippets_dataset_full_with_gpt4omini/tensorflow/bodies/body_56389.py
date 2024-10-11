# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
config.set_soft_device_placement(False)
gpus = config.list_physical_devices('GPU')
self.assertGreater(len(gpus), 0)

cpus = config.list_physical_devices('CPU')
self.assertEqual(len(cpus), 1)

self.assertEqual(len(config.get_visible_devices('CPU')), 1)
self.assertGreater(len(config.get_visible_devices('GPU')), 0)

self.assertEqual(len(config.get_visible_devices('XLA_GPU')), 0)

config.set_visible_devices(cpus[0])
self.assertEqual(len(config.get_visible_devices('CPU')), 1)
self.assertEqual(len(config.get_visible_devices('GPU')), 0)
self.assertEqual(len(config.list_logical_devices('XLA_GPU')), 0)

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Could not satisfy'):
    with ops.device('/device:GPU:0'):
        a = array_ops.identity(1.0)
        self.evaluate(a)

    # Modifying the visible devices is not supported
with self.assertRaisesRegex(RuntimeError, 'cannot be modified'):
    config.set_visible_devices(gpus)

# Setting the same visible devices is fine
config.set_visible_devices(cpus[0])
