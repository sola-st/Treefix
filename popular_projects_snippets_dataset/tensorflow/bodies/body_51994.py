# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
actual = fc.make_parse_example_spec([])
self.assertDictEqual({}, actual)
