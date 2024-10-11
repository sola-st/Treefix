# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
wire_column = fc.categorical_column_with_hash_bucket('wire', 4)
self.assertEqual(['wire'], wire_column.parents)

config = wire_column.get_config()
self.assertEqual({
    'key': 'wire',
    'hash_bucket_size': 4,
    'dtype': 'string'
}, config)

self.assertEqual(wire_column,
                 fc.HashedCategoricalColumn.from_config(config))
