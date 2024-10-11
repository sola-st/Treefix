# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
with self.assertRaisesRegex(ValueError, 'Failed parsing device name'):
    context.context().get_memory_info('GPU')
with self.assertRaisesRegex(ValueError, 'Failed parsing device name'):
    context.context().get_memory_info('GPU:')
with self.assertRaisesRegex(ValueError, 'Failed parsing device name'):
    context.context().get_memory_info('GPU:CPU')
