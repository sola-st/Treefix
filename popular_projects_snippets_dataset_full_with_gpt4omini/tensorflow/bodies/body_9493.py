# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
del self.wrapped_flags.test
self.assertNotIn('test', self.wrapped_flags)
with self.assertRaises(AttributeError):
    _ = self.wrapped_flags.test
