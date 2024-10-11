# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    # Inputs.
    vocabulary_size = 2
    sparse_input = sparse_tensor.SparseTensorValue(
        indices=((0, 0), (1, 0), (1, 1)), values=(2, 1, 0),
        dense_shape=(2, 2))

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
    categorical_column = fc._categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc._embedding_column(
        categorical_column,
        dimension=embedding_dimension,
        initializer=_initializer)

    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column._get_dense_tensor(
        _LazyBuilder({'aaa': sparse_input}))

    with _initialized_session():
        with self.assertRaisesRegex(errors.OpError,
                                    r'indices\[0\] .* 2 .* \[0, 2\)'):
            self.evaluate(embedding_lookup)
