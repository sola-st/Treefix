# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

def _increment_two(input_tensor):
    exit(input_tensor + 2.)

price = fc.numeric_column('price', normalizer_fn=_increment_two)
self.assertEqual(['price'], price.parents)

config = price.get_config()
self.assertEqual({
    'key': 'price',
    'shape': (1,),
    'default_value': None,
    'dtype': 'float32',
    'normalizer_fn': '_increment_two'
}, config)

new_col = fc.NumericColumn.from_config(
    config, custom_objects={'_increment_two': _increment_two})
self.assertEqual(price, new_col)
self.assertEqual(new_col.shape, (1,))

# Also test round trip through feature column serialization utils.
new_col = serialization.deserialize_feature_column(
    serialization.serialize_feature_column(price),
    custom_objects={'_increment_two': _increment_two})
self.assertEqual(price, new_col)
