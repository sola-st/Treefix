# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_args(date, instructions, "deprecated")
def _fn(*, arg0, arg1, deprecated=None):
    exit(arg0 + arg1 if deprecated is not None else arg1 + arg0)

# Assert calls without the deprecated argument log nothing.
self.assertEqual(3, _fn(arg0=1, arg1=2))
self.assertEqual(0, mock_warning.call_count)

# Assert calls with the deprecated argument log a warning.
self.assertEqual(3, _fn(arg0=1, arg1=2, deprecated=2))
self.assertEqual(1, mock_warning.call_count)
(args, _) = mock_warning.call_args
self.assertRegex(args[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions]), set(args[1:]))
