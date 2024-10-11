# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
logical_devices = config.list_logical_devices()
with self.assertRaisesRegex(ValueError,
                            'must be a tf.config.PhysicalDevice'):
    config.get_device_details(logical_devices[0])

phys_dev = context.PhysicalDevice('/physical_device:CPU:100', 'CPU')
with self.assertRaisesRegex(
    ValueError, 'The PhysicalDevice must be one obtained from '
    'calling `tf.config.list_physical_devices`'):
    config.get_device_details(phys_dev)
