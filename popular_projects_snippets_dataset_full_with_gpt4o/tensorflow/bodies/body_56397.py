# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
if test_util.IsMklEnabled():
    # TODO(gzmkl) work with Google team to address design issue in allocator.h
    self.skipTest('MklCPUAllocator does not throw exception. So skip test.')

with self.assertRaisesRegex(ValueError, 'Allocator stats not available'):
    config.get_memory_info('CPU:0')
with self.assertRaisesRegex(ValueError, 'Allocator stats not available'):
    config.get_memory_usage('CPU:0')
