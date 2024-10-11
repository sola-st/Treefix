# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
with self.assertRaisesRegex(ValueError, 'No matching devices found'):
    config.reset_memory_stats('unknown_device:0')
