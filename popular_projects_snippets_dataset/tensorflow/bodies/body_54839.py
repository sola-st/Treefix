# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
self.assertEqual(v1.most_specific_common_supertype([v2]), result)
self.assertEqual(v2.most_specific_common_supertype([v1]), result)
