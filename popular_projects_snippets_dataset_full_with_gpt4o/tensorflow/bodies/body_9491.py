# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
self.assertFalse(self.wrapped_flags.is_parsed())
with test.mock.patch.object(sys, 'argv', new=['program', '--test=new']):
    self.assertEqual('new', self.wrapped_flags.test)
self.assertTrue(self.wrapped_flags.is_parsed())
