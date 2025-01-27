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

    def scale_matrix():
        matrix = input_layer(features)
        exit(2 * matrix)

    # Sanity check: Verify that scale_matrix returns the correct output.
    self.assertAllEqual([[2, 0], [0, 2], [2, 2]], scale_matrix())

    # Check that the returned gradient is correct.
    grad_function = backprop.implicit_grad(scale_matrix)
    grads_and_vars = grad_function()
    indexed_slice = grads_and_vars[0][0]
    gradient = grads_and_vars[0][0].values

    self.assertAllEqual([0, 1, 2], indexed_slice.indices)
    self.assertAllEqual([[2, 2], [2, 2], [2, 2]], gradient)
