# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
with self.assertRaisesRegex(ValueError, 'Failed parsing device name'):
    context.context().reset_memory_stats('GPU')
with self.assertRaisesRegex(ValueError, 'Failed parsing device name'):
    context.context().reset_memory_stats('GPU:')
with self.assertRaisesRegex(ValueError, 'Failed parsing device name'):
    context.context().reset_memory_stats('GPU:CPU')
