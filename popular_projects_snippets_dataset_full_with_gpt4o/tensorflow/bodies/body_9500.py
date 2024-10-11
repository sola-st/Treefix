# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
self.wrapped_flags(['program', '--test=new'])
self.assertEqual('new', self.wrapped_flags.test)
