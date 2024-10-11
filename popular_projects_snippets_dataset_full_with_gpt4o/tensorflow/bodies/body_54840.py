# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
self.assertIsNone(v1.most_specific_common_supertype([v2]))
self.assertIsNone(v2.most_specific_common_supertype([v1]))
