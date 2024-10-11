# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
self.assertEqual(v1.most_specific_compatible_type(v2), expected)
self.assertEqual(v2.most_specific_compatible_type(v1), expected)
