# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
categorical_column = fc.categorical_column_with_identity(
    key='ids', num_buckets=3)
column = fc.weighted_categorical_column(
    categorical_column=categorical_column, weight_feature_key='weight')

self.assertEqual([categorical_column, 'weight'], column.parents)

config = column.get_config()
self.assertEqual({
    'categorical_column': {
        'config': {
            'key': 'ids',
            'number_buckets': 3,
            'default_value': None
        },
        'class_name': 'IdentityCategoricalColumn'
    },
    'dtype': 'float32',
    'weight_feature_key': 'weight'
}, config)

self.assertEqual(column, fc.WeightedCategoricalColumn.from_config(config))

new_column = fc.WeightedCategoricalColumn.from_config(
    config,
    columns_by_name={
        serialization._column_name_with_class_name(categorical_column):
            categorical_column
    })
self.assertEqual(column, new_column)
self.assertIs(categorical_column, new_column.categorical_column)
