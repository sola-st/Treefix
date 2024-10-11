# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
gpus = config.list_physical_devices('GPU')
self.assertNotEqual(len(gpus), 0)

self.assertIsNone(config.get_memory_growth(gpus[-1]))
for gpu in gpus:
    config.set_memory_growth(gpu, True)

c = context.context().config
self.assertTrue(c.gpu_options.allow_growth)

logical_gpus = config.list_logical_devices('GPU')
self.assertTrue(len(logical_gpus), len(gpus))

# Modifying the GPU configuration is not supported
with self.assertRaisesRegex(RuntimeError, 'cannot be modified'):
    for gpu in gpus:
        config.set_memory_growth(gpu, False)

    # Setting the same GPU configuration is fine
for gpu in gpus:
    config.set_memory_growth(gpu, True)
