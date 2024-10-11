# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
self.assertEqual('default', self.wrapped_flags.test)
self.wrapped_flags.test = 'new'
self.assertEqual('new', self.wrapped_flags.test)
