# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
key1 = 'key1'
parse_spec1 = parsing_ops.FixedLenFeature(
    shape=(2,), dtype=dtypes.float32, default_value=0.)
with self.assertRaisesRegex(
    ValueError,
    'All feature_columns must be _FeatureColumn instances.*invalid_column'):
    fc.make_parse_example_spec(
        (self._TestFeatureColumn({key1: parse_spec1}), 'invalid_column'))  # pylint: disable=abstract-class-instantiated
