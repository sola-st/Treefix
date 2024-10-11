# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated(date, instructions, warn_once=False)
def _fn():
    pass

_fn()
self.assertEqual(1, mock_warning.call_count)

with deprecation.silence():
    _fn()
self.assertEqual(1, mock_warning.call_count)

_fn()
self.assertEqual(2, mock_warning.call_count)
