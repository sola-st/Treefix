# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
actual = fc.make_parse_example_spec_v2([])
self.assertDictEqual({}, actual)
