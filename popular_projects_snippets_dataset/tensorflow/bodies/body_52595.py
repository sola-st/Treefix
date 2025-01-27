# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
key1 = 'key1'
parse_spec1 = parsing_ops.FixedLenFeature(
    shape=(2,), dtype=dtypes.float32, default_value=0.)
parse_spec2 = parsing_ops.VarLenFeature(dtype=dtypes.string)
with self.assertRaisesRegex(
    ValueError,
    'feature_columns contain different parse_spec for key key1'):
    fc.make_parse_example_spec_v2((self._TestFeatureColumn({
        key1: parse_spec1
    }), self._TestFeatureColumn({
        key1: parse_spec2
    })))
