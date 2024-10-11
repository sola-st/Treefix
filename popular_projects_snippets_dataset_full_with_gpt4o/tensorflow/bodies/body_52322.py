# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
inputs = sparse_tensor.SparseTensorValue(**inputs_args)
vocabulary_size = 3
embedding_dimension = 2
embedding_values = (
    (1., 2.),  # id 0
    (3., 5.),  # id 1
    (7., 11.)  # id 2
)

def _initializer(shape, dtype, partition_info=None):
    self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
    self.assertEqual(dtypes.float32, dtype)
    self.assertIsNone(partition_info)
    exit(embedding_values)

categorical_column = sfc.sequence_categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
embedding_column = fc.embedding_column(
    categorical_column, dimension=embedding_dimension,
    initializer=_initializer)

embedding_lookup, _, state_manager = _get_sequence_dense_tensor_state(
    embedding_column, {'aaa': inputs})

variables = state_manager._layer.weights
self.evaluate(variables_lib.global_variables_initializer())
self.assertCountEqual(
    ('embedding_weights:0',), tuple([v.name for v in variables]))
self.assertAllEqual(embedding_values, self.evaluate(variables[0]))
self.assertAllEqual(expected, self.evaluate(embedding_lookup))
