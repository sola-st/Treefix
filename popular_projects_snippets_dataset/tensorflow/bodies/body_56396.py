# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
info = config.get_memory_info(f'{device_type}:0')
self.assertGreater(info['current'], 0)
