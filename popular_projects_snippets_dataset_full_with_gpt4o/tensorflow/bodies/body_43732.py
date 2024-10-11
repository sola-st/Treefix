# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_arg_values(date, instructions, warn_once=True,
                                   deprecated=True)
def _fn(deprecated):  # pylint: disable=unused-argument
    pass

_fn(deprecated=False)
self.assertEqual(0, mock_warning.call_count)
_fn(deprecated=True)
self.assertEqual(1, mock_warning.call_count)
_fn(deprecated=True)
self.assertEqual(1, mock_warning.call_count)
