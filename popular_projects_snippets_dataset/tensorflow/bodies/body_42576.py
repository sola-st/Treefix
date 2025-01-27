# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
if test_util.IsMklEnabled():
    # TODO(gzmkl) work with Google team to address design issue in allocator.h
    self.skipTest('MklCPUAllocator does not throw exception. So skip test.')

with self.assertRaisesRegex(ValueError, 'Allocator stats not available'):
    context.context().get_memory_info('CPU:0')
