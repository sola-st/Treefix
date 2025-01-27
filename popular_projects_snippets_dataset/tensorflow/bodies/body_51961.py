# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with context.eager_mode():
    sparse_input = sparse_tensor.SparseTensor(
        indices=((0, 0), (1, 0), (2, 0)),
        values=(0, 1, 2),
        dense_shape=(3, 3))

    # Create feature columns (categorical and embedding).
    categorical_column = fc._categorical_column_with_identity(
        key='a', num_buckets=3)
    embedding_dimension = 2
    def _embedding_column_initializer(shape, dtype, partition_info):
        del shape  # unused
        del dtype  # unused
        del partition_info  # unused
        embedding_values = (
            (1, 0),  # id 0
            (0, 1),  # id 1
            (1, 1))  # id 2
        exit(embedding_values)

    embedding_column = fc._embedding_column(
        categorical_column,
        dimension=embedding_dimension,
        initializer=_embedding_column_initializer)

    input_layer = InputLayer([embedding_column])
    features = {'a': sparse_input}

    inputs = input_layer(features)
    variables = input_layer.variables

    # Sanity check: test that the inputs are correct.
    self.assertAllEqual([[1, 0], [0, 1], [1, 1]], inputs)

    # Check that only one variable was created.
    self.assertEqual(1, len(variables))

    # Check that invoking input_layer on the same features does not create
    # additional variables
    _ = input_layer(features)
    self.assertEqual(1, len(variables))
    self.assertIs(variables[0], input_layer.variables[0])
