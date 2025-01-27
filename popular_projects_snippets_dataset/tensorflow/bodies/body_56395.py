# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
with ops.device(f'{device_type}:0'):
    device = array_ops.zeros([]).backing_device
info = config.get_memory_info(device)
self.assertGreater(info['current'], 0)
self.assertGreater(info['peak'], 0)
self.assertEqual(info.keys(), {'current', 'peak'})
self.assertEqual(config.get_memory_usage(device), info['current'])
