# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
self.original_flags = flags.FlagValues()
self.wrapped_flags = flags._FlagValuesWrapper(self.original_flags)
flags.DEFINE_string(
    'test', 'default', 'test flag', flag_values=self.wrapped_flags)
