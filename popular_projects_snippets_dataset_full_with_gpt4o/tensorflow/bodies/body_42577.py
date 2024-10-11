# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
with self.assertRaisesRegex(ValueError, 'No matching devices found'):
    context.context().get_memory_info('unknown_device:0')
