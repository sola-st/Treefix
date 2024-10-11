# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_identity(key='aaa', num_buckets=3)

self.assertEqual(['aaa'], column.parents)

config = column.get_config()
self.assertEqual({
    'default_value': None,
    'key': 'aaa',
    'number_buckets': 3
}, config)

self.assertEqual(column, fc.IdentityCategoricalColumn.from_config(config))
