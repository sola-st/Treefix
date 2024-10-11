# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""parse_spc for one column is a dict with length > 1."""
key1 = 'key1'
parse_spec1 = parsing_ops.FixedLenFeature(
    shape=(2,), dtype=dtypes.float32, default_value=0.)
key2 = 'key2'
parse_spec2 = parsing_ops.VarLenFeature(dtype=dtypes.string)
key3 = 'key3'
parse_spec3 = parsing_ops.VarLenFeature(dtype=dtypes.int32)
actual = fc.make_parse_example_spec_v2((self._TestFeatureColumn({
    key1: parse_spec1
}), self._TestFeatureColumn({
    key2: parse_spec2,
    key3: parse_spec3
})))
self.assertDictEqual({
    key1: parse_spec1,
    key2: parse_spec2,
    key3: parse_spec3
}, actual)
