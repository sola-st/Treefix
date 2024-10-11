# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
flag = flags.Flag(flags.ArgumentParser(), flags.ArgumentSerializer(),
                  'fruit', 'apple', 'the fruit type')
self.wrapped_flags['fruit'] = flag
self.assertIs(self.original_flags['fruit'], self.wrapped_flags['fruit'])
self.assertEqual('apple', self.wrapped_flags.fruit)
