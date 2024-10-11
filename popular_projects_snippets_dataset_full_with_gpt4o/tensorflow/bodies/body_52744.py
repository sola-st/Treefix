# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    # Inputs.
    vocabulary_size = 3
    # -1 values are ignored.
    input_a = np.array([
        [2, 1],  # example 0, ids [2, 1]
        [0, -1]
    ])  # example 1, ids [0]
    input_b = np.array([
        [1, -1],  # example 0, ids [1]
        [1, 2]
    ])  # example 1, ids [1, 2]
    input_features = {'aaa': input_a, 'bbb': input_b}

    # Embedding variable.
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

    # Expected lookup result, using combiner='mean'.
    expected_lookups_a = (
        # example 0:
        (5., 8.),  # ids [2, 1], embedding =  mean([3, 5] + [7, 11]) = [5, 8]
        # example 1:
        (1., 2),  # ids [0], embedding = [1, 2]
    )
    expected_lookups_b = (
        # example 0:
        (3., 5.),  # ids [1], embedding = [3, 5]
        # example 1:
        (5., 8.),  # ids [1, 2], embedding = mean([3, 5] + [7, 11]) = [5, 8]
    )

    # Build columns.
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)
    embedding_column_a, embedding_column_b = fc.shared_embedding_columns_v2(
        [categorical_column_a, categorical_column_b],
        dimension=embedding_dimension,
        initializer=_initializer,
        use_safe_embedding_lookup=use_safe_embedding_lookup)

    # Provide sparse input and get dense result.
    embedding_lookup_a = embedding_column_a.get_dense_tensor(
        fc.FeatureTransformationCache(input_features), None)
    embedding_lookup_b = embedding_column_b.get_dense_tensor(
        fc.FeatureTransformationCache(input_features), None)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertCountEqual(('aaa_bbb_shared_embedding:0',),
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
