# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_args(date, instructions, "arg", warn_once=True)
def _fn(arg=0):  # pylint: disable=unused-argument
    pass

_fn()
self.assertEqual(0, mock_warning.call_count)
_fn(arg=0)
self.assertEqual(1, mock_warning.call_count)
_fn(arg=1)
self.assertEqual(1, mock_warning.call_count)
