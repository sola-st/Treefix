# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
actual = dynamic_ragged_shape._find_dtype(3, None)
self.assertIsNone(actual)
