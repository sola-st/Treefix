# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
key1 = 'key1'
parse_spec1 = parsing_ops.FixedLenFeature(
    shape=(2,), dtype=dtypes.float32, default_value=0.)
key2 = 'key2'
parse_spec2 = parsing_ops.VarLenFeature(dtype=dtypes.string)
actual = fc.make_parse_example_spec((
    self._TestFeatureColumn({key1: parse_spec1}),  # pylint: disable=abstract-class-instantiated
    self._TestFeatureColumn({key2: parse_spec2})))  # pylint: disable=abstract-class-instantiated
self.assertDictEqual({key1: parse_spec1, key2: parse_spec2}, actual)
