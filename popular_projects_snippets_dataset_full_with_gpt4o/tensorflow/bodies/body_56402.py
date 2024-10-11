# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
if test_util.IsMklEnabled():
    # TODO(gzmkl) work with Google team to address design issue in allocator.h
    self.skipTest('MklCPUAllocator does not throw exception. So skip test.')

with self.assertRaisesRegex(ValueError, 'Cannot reset memory stats'):
    config.reset_memory_stats('CPU:0')
