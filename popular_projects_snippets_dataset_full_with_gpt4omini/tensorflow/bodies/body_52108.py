# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    # Inputs.
    vocabulary_size = 4
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1
        (7., 11.),  # id 2
        (9., 13.)  # id 3
    )

    def _initializer(shape, dtype, partition_info=None):
        if partition_variables:
            self.assertEqual([vocabulary_size, embedding_dimension],
                             partition_info.full_shape)
            self.assertAllEqual((2, embedding_dimension), shape)
        else:
            self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
            self.assertIsNone(partition_info)

        self.assertEqual(dtypes.float32, dtype)
        exit(embedding_values)

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc._categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    partitioner = None
    if partition_variables:
        partitioner = partitioned_variables.fixed_size_partitioner(2, axis=0)
    with variable_scope.variable_scope('vars', partitioner=partitioner):
        embedding_column = fc._embedding_column(
            categorical_column,
            dimension=embedding_dimension,
            initializer=_initializer,
            use_safe_embedding_lookup=use_safe_embedding_lookup)

        # Provide sparse input and get dense result.
        embedding_lookup = embedding_column._get_dense_tensor(
            _LazyBuilder({'aaa': sparse_input}))

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    if partition_variables:
        self.assertCountEqual(('vars/embedding_weights/part_0:0',
                               'vars/embedding_weights/part_1:0'),
                              tuple([v.name for v in global_vars]))
    else:
        self.assertCountEqual(('vars/embedding_weights:0',),
                              tuple([v.name for v in global_vars]))
    for v in global_vars:
        self.assertIsInstance(v, variables_lib.Variable)
    with _initialized_session():
        self.assertAllEqual(embedding_values, global_vars[0])
        self.assertAllEqual(expected_lookups, self.evaluate(embedding_lookup))

    if use_safe_embedding_lookup:
        self.assertIn(
            'SparseFillEmptyRows',
            [x.type for x in ops.get_default_graph().get_operations()])
    else:
        self.assertNotIn(
            'SparseFillEmptyRows',
            [x.type for x in ops.get_default_graph().get_operations()])
