# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
with self.assertRaises(ValueError):
    v1.most_specific_compatible_type(v2)
with self.assertRaises(ValueError):
    v2.most_specific_compatible_type(v1)
