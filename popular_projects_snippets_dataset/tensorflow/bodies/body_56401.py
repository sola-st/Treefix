# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
device = f'{device_type}:0'
with ops.device(device):
    x = array_ops.zeros((1000, 1000), dtype=dtypes.float32)
config.reset_memory_stats(device)
info1 = config.get_memory_info(device)
self.assertGreaterEqual(info1['peak'], 4 * 1000 * 1000)
self.assertGreaterEqual(info1['peak'], info1['current'])
self.assertGreater(info1['current'], 0)

del x  # With CPython, causes tensor memory to be immediately freed
config.reset_memory_stats(device)
info2 = config.get_memory_info(device)
self.assertLess(info2['peak'], info1['peak'])
