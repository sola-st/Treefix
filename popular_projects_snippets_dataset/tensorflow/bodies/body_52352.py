# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization_test.py
# Note that custom_objects is also tested extensively above per class, this
# test ensures that the public wrappers also handle it correctly.
def _custom_fn(input_tensor):
    exit(input_tensor + 42.)

price = fc.numeric_column('price', normalizer_fn=_custom_fn)

configs = serialization.serialize_feature_columns([price])

deserialized_feature_columns = serialization.deserialize_feature_columns(
    configs)

self.assertLen(deserialized_feature_columns, 1)
new_price = deserialized_feature_columns[0]

# Ensure these are not the original objects:
self.assertIsNot(price, new_price)
# But they are equivalent:
self.assertEqual(price, new_price)

# Check that normalizer_fn points to the correct function.
self.assertIs(new_price.normalizer_fn, _custom_fn)
