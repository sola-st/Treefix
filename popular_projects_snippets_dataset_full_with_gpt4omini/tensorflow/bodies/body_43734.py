# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_arg_values(date, instructions, warn_once=True,
                                   arg0="forbidden", arg1="disallowed")
def _fn(arg0, arg1):  # pylint: disable=unused-argument
    pass

_fn(arg0="allowed", arg1="also allowed")
self.assertEqual(0, mock_warning.call_count)
_fn(arg0="forbidden", arg1="disallowed")
self.assertEqual(2, mock_warning.call_count)
_fn(arg0="forbidden", arg1="allowed")
self.assertEqual(2, mock_warning.call_count)
_fn(arg0="forbidden", arg1="disallowed")
self.assertEqual(2, mock_warning.call_count)
