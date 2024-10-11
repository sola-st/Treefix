# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    # Inputs.
    vocabulary_size = 4
    # -1 values are ignored.
    input_a = np.array([
        [2, -1, -1],  # example 0, ids [2]
        [0, 1, -1]
    ])  # example 1, ids [0, 1]
    input_b = np.array([
        [0, -1, -1],  # example 0, ids [0]
        [-1, -1, -1]
    ])  # example 1, ids []
    input_features = {'aaa': input_a, 'bbb': input_b}

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
    expected_lookups_a = (
        # example 0:
        (7., 11.),  # ids [2], embedding = [7, 11]
        # example 1:
        (2., 3.5),  # ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
    )
    if use_safe_embedding_lookup:
        expected_lookups_b = (
            # example 0:
            (1., 2.),  # ids [0], embedding = [1, 2]
            # example 1:
            (0., 0.),  # ids [], embedding = [0, 0]
        )
    else:
        expected_lookups_b = (
            # example 0:
            (1., 2.),  # ids [0], embedding = [1, 2]
        )

    # Build columns.
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)

    partitioner = None
    if partition_variables:
        partitioner = partitioned_variables.fixed_size_partitioner(2, axis=0)

    with variable_scope.variable_scope('vars', partitioner=partitioner):
        embedding_column_a, embedding_column_b = (
            fc_new.shared_embedding_columns(
                [categorical_column_a, categorical_column_b],
                dimension=embedding_dimension,
                initializer=_initializer,
                use_safe_embedding_lookup=use_safe_embedding_lookup))
        # Provide sparse input and get dense result.
        embedding_lookup_a = embedding_column_a._get_dense_tensor(
            _LazyBuilder(input_features))
        embedding_lookup_b = embedding_column_b._get_dense_tensor(
            _LazyBuilder(input_features))
    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    if partition_variables:
        self.assertCountEqual(('vars/embedding_weights/part_0:0',
                               'vars/embedding_weights/part_1:0'),
                              tuple([v.name for v in global_vars]))
    else:
        self.assertCountEqual(('vars/embedding_weights:0',),
                              tuple([v.name for v in global_vars]))
    embedding_var = global_vars[0]

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllEqual(embedding_values, self.evaluate(embedding_var))
    self.assertAllEqual(expected_lookups_a, self.evaluate(embedding_lookup_a))
    self.assertAllEqual(expected_lookups_b, self.evaluate(embedding_lookup_b))

    if use_safe_embedding_lookup:
        self.assertIn(
            'SparseFillEmptyRows',
            [x.type for x in ops.get_default_graph().get_operations()])
    else:
        self.assertNotIn(
            'SparseFillEmptyRows',
            [x.type for x in ops.get_default_graph().get_operations()])
