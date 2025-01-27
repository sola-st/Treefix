# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    # Inputs.
    vocabulary_size = 3
    # -1 values are ignored.
    input_a = np.array([
        [2, -1, -1],  # example 0, ids [2]
        [0, 1, -1]
    ])  # example 1, ids [0, 1]
    input_b = np.array([
        [0, -1, -1],  # example 0, ids [0]
        [-1, -1, -1]
    ])  # example 1, ids []
    # Specify shape, because dense input must have rank specified.
    input_a_placeholder = array_ops.placeholder(
        dtype=dtypes.int64, shape=[None, 3])
    input_b_placeholder = array_ops.placeholder(
        dtype=dtypes.int64, shape=[None, 3])
    input_features = {
        'aaa': input_a_placeholder,
        'bbb': input_b_placeholder,
    }
    feed_dict = {
        input_a_placeholder: input_a,
        input_b_placeholder: input_b,
    }

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
    if use_safe_embedding_lookup:
        self.assertIn(
            'SparseFillEmptyRows',
            [x.type for x in ops.get_default_graph().get_operations()])
    else:
        self.assertNotIn(
            'SparseFillEmptyRows',
            [x.type for x in ops.get_default_graph().get_operations()])

    with _initialized_session() as sess:
        sess.run([embedding_lookup_a, embedding_lookup_b], feed_dict=feed_dict)
