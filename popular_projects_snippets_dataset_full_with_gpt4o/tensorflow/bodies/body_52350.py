# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization_test.py
price = fc.numeric_column('price')
bucketized_price = fc.bucketized_column(price, boundaries=[0, 1])

configs = serialization.serialize_feature_columns([price, bucketized_price])

deserialized_feature_columns = serialization.deserialize_feature_columns(
    configs)
self.assertLen(deserialized_feature_columns, 2)
new_price = deserialized_feature_columns[0]
new_bucketized_price = deserialized_feature_columns[1]

# Ensure these are not the original objects:
self.assertIsNot(price, new_price)
self.assertIsNot(bucketized_price, new_bucketized_price)
# But they are equivalent:
self.assertEqual(price, new_price)
self.assertEqual(bucketized_price, new_bucketized_price)

# Check that deduping worked:
self.assertIs(new_bucketized_price.source_column, new_price)
