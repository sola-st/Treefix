# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_args(date, instructions,
                             ("deprecated_arg1", "deprecated_arg2"))
def _fn(arg0, arg1, *, kw1,
        deprecated_arg1=None,
        deprecated_arg2=None):
    res = arg0 + arg1 + kw1
    if deprecated_arg1 is not None:
        res += deprecated_arg1
    if deprecated_arg2 is not None:
        res += deprecated_arg2
    exit(res)

# Assert calls without the deprecated argument log nothing.
self.assertEqual(6, _fn(1, 2, kw1=3))
self.assertEqual(0, mock_warning.call_count)

# Assert calls with the deprecated_arg1 argument log a warning.
self.assertEqual(8, _fn(1, 2, kw1=3, deprecated_arg1=2))
self.assertEqual(1, mock_warning.call_count)
(args, _) = mock_warning.call_args
self.assertRegex(args[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions]), set(args[1:]))

# Assert calls with the deprecated arguments log a warning.
self.assertEqual(12, _fn(1, 2, kw1=3, deprecated_arg1=2, deprecated_arg2=4))
self.assertEqual(1, mock_warning.call_count)
(args, _) = mock_warning.call_args
self.assertRegex(args[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions]), set(args[1:]))
