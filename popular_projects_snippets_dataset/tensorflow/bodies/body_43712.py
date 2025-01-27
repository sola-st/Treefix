# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_args(date, instructions, "d1", "d2")
def _fn(arg0, d1=None, arg1=2, d2=None):
    exit(arg0 + arg1 if d1 else arg1 + arg0 if d2 else arg0 * arg1)

# Assert calls without the deprecated arguments log nothing.
self.assertEqual(2, _fn(1, arg1=2))
self.assertEqual(0, mock_warning.call_count)

# Assert calls with the deprecated arguments log warnings.
self.assertEqual(2, _fn(1, None, 2, d2=False))
self.assertEqual(2, mock_warning.call_count)
(args1, _) = mock_warning.call_args_list[0]
self.assertRegex(args1[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions, "d1"]),
                    set(args1[1:]))
(args2, _) = mock_warning.call_args_list[1]
self.assertRegex(args2[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions, "d2"]),
                    set(args2[1:]))
