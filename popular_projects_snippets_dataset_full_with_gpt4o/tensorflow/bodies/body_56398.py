# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
with self.assertRaisesRegex(ValueError, 'No matching devices found'):
    config.get_memory_info('unknown_device:0')
with self.assertRaisesRegex(ValueError, 'No matching devices found'):
    config.get_memory_usage('unknown_device:0')
