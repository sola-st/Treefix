# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated(date, instructions, warn_once=True)
def _fn():
    pass

_fn()
self.assertEqual(1, mock_warning.call_count)
_fn()
self.assertEqual(1, mock_warning.call_count)
