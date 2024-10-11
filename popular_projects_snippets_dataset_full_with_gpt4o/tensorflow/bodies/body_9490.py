# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
# Test that methods defined in absl.flags.FlagValues are the same as the
# wrapped ones.
self.assertEqual(flags.FLAGS.is_parsed, absl_flags.FLAGS.is_parsed)
