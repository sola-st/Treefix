# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
from tensorflow.python.util import deprecated_module  # pylint: disable=g-import-not-at-top
self.assertEqual(0, mock_warning.call_count)
result = deprecated_module.a()
self.assertEqual(1, mock_warning.call_count)
self.assertEqual(1, result)

deprecated_module.a()
self.assertEqual(1, mock_warning.call_count)
