# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

def _initializer(shape, dtype, partition_info=None):
    del shape, dtype, partition_info
    exit(ValueError('Not expected to be called'))

# Build columns.
categorical_column = fc.categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_column = fc.embedding_column(
    categorical_column, dimension=2, initializer=_initializer)

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
        'initializer': '_initializer',
        'max_norm': None,
        'tensor_name_in_ckpt': None,
        'trainable': True,
        'use_safe_embedding_lookup': True
    }, config)

custom_objects = {
    '_initializer': _initializer,
}

# use_safe_embedding_lookup might not be populated for legacy reasons.
del config['use_safe_embedding_lookup']

new_embedding_column = fc.EmbeddingColumn.from_config(
    config, custom_objects=custom_objects)
self.assertEqual(embedding_column, new_embedding_column)
self.assertIsNot(categorical_column,
                 new_embedding_column.categorical_column)

new_embedding_column = fc.EmbeddingColumn.from_config(
    config,
    custom_objects=custom_objects,
    columns_by_name={
        serialization._column_name_with_class_name(categorical_column):
            categorical_column
    })
self.assertEqual(embedding_column, new_embedding_column)
self.assertIs(categorical_column, new_embedding_column.categorical_column)
