# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
self.assertFalse(v1.is_compatible_with(v2))
self.assertFalse(v2.is_compatible_with(v1))
