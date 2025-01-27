# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
device = f'{device_type}:0'
with ops.device(device):
    x1 = array_ops.zeros((1000, 1000))
peak1 = config.get_memory_info(device)['peak']
self.assertGreaterEqual(peak1, 4 * 1000 * 1000)
with ops.device(device):
    x2 = array_ops.ones((1000, 1000))
peak2 = config.get_memory_info(device)['peak']
self.assertGreaterEqual(peak2, peak1 + 4 * 1000 * 1000)
del x1, x2  # With CPython, causes tensor memory to be immediately freed
peak3 = config.get_memory_info(device)['peak']
self.assertGreaterEqual(peak3, peak2)
self.assertGreaterEqual(peak3, config.get_memory_info(device)['current'])
