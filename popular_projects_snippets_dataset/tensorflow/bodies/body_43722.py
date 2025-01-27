# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_args(date, instructions, "arg0", "arg1",
                             warn_once=True)
def _fn(arg0=0, arg1=0):  # pylint: disable=unused-argument
    pass

_fn(arg0=0)
self.assertEqual(1, mock_warning.call_count)
_fn(arg0=0)
self.assertEqual(1, mock_warning.call_count)
_fn(arg1=0)
self.assertEqual(2, mock_warning.call_count)
_fn(arg0=0)
self.assertEqual(2, mock_warning.call_count)
_fn(arg1=0)
self.assertEqual(2, mock_warning.call_count)
