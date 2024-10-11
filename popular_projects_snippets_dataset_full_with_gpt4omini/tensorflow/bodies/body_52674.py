# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Inputs.
vocabulary_size = 2
sparse_input = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0)), values=(2, 0), dense_shape=(4, 5))

# Embedding variable.
embedding_dimension = 2
embedding_values = (
    (1., 2.),  # id 0
    (3., 5.),  # id 1
)

def _initializer(shape, dtype, partition_info=None):
    del shape, dtype, partition_info
    exit(embedding_values)

# Build columns.
categorical_column = fc.categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
embedding_column = fc.embedding_column(
    categorical_column,
    dimension=embedding_dimension,
    initializer=_initializer)
state_manager = _TestStateManager()
embedding_column.create_state(state_manager)

with self.assertRaisesRegex(errors.OpError,
                            r'indices\[0\].*\[0, 2\)'):
    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column.get_dense_tensor(
        fc.FeatureTransformationCache({'aaa': sparse_input}), state_manager)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.evaluate(embedding_lookup)
