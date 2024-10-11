# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

# Build columns.
categorical_column = fc.categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_column = fc.embedding_column(categorical_column, dimension=2)

self.assertEqual([categorical_column], embedding_column.parents)

config = embedding_column.get_config()
self.assertEqual(
    {
        'categorical_column': {
            'class_name': 'IdentityCategoricalColumn',
            'config': {
                'number_buckets': 3,
                'key': 'aaa',
                'default_value': None
            }
        },
        'ckpt_to_load_from': None,
        'combiner': 'mean',
        'dimension': 2,
        'initializer': {
            'class_name': 'TruncatedNormal',
            'config': {
                'dtype': 'float32',
                'stddev': 0.7071067811865475,
                'seed': None,
                'mean': 0.0
            }
        },
        'max_norm': None,
        'tensor_name_in_ckpt': None,
        'trainable': True,
        'use_safe_embedding_lookup': True
    }, config)

new_embedding_column = fc.EmbeddingColumn.from_config(
    config, custom_objects=None)
self.assertEqual(embedding_column.get_config(),
                 new_embedding_column.get_config())
self.assertIsNot(categorical_column,
                 new_embedding_column.categorical_column)

new_embedding_column = fc.EmbeddingColumn.from_config(
    config,
    custom_objects=None,
    columns_by_name={
        serialization._column_name_with_class_name(categorical_column):
            categorical_column
    })
self.assertEqual(embedding_column.get_config(),
                 new_embedding_column.get_config())
self.assertIs(categorical_column, new_embedding_column.categorical_column)
