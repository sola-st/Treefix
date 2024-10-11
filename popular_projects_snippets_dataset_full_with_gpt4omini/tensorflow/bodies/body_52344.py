# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests that column can be serialized."""
def _custom_fn(input_tensor):
    exit(input_tensor + 42)

column = sfc.sequence_numeric_column(
    key='my-key', shape=(2,), default_value=3, dtype=dtypes.int32,
    normalizer_fn=_custom_fn)
configs = serialization.serialize_feature_column(column)
column = serialization.deserialize_feature_column(
    configs, custom_objects={_custom_fn.__name__: _custom_fn})
self.assertEqual(column.key, 'my-key')
self.assertEqual(column.shape, (2,))
self.assertEqual(column.default_value, 3)
self.assertEqual(column.normalizer_fn(3), 45)
with self.assertRaisesRegex(ValueError,
                            'Instance: 0 is not a FeatureColumn'):
    serialization.serialize_feature_column(int())
