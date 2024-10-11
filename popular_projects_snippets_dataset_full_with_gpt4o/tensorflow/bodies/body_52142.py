# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    # Inputs.
    vocabulary_size = 3
    sparse_input_a = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        indices=((0, 0), (1, 0), (1, 4)),
        values=(2, 0, 1),
        dense_shape=(2, 5))
    sparse_input_b = sparse_tensor.SparseTensorValue(
        # example 0, ids [0]
        # example 1, ids []
        indices=((0, 0),),
        values=(0,),
        dense_shape=(2, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1
        (7., 11.)  # id 2
    )

    def _initializer(shape, dtype, partition_info):
        self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
        self.assertEqual(dtypes.float32, dtype)
        self.assertIsNone(partition_info)
        exit(embedding_values)

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0:
        # A ids [2], embedding = [7, 11]
        # B ids [0], embedding = [1, 2]
        (7., 11., 1., 2.),
        # example 1:
        # A ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        # B ids [], embedding = [0, 0]
        (2., 3.5, 0., 0.),
    )

    # Build columns.
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)
    embedding_column_a, embedding_column_b = fc_new.shared_embedding_columns(
        [categorical_column_a, categorical_column_b],
        dimension=embedding_dimension,
        initializer=_initializer,
        trainable=trainable)

    # Provide sparse input and get dense result.
    input_layer = fc.input_layer(
        features={
            'aaa': sparse_input_a,
            'bbb': sparse_input_b
        },
        feature_columns=(embedding_column_b, embedding_column_a))

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertCountEqual(
        ['input_layer/aaa_bbb_shared_embedding/embedding_weights:0'],
        tuple([v.name for v in global_vars]))
    trainable_vars = ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    if trainable:
        self.assertCountEqual(
            ['input_layer/aaa_bbb_shared_embedding/embedding_weights:0'],
            tuple([v.name for v in trainable_vars]))
    else:
        self.assertCountEqual([], tuple([v.name for v in trainable_vars]))
    shared_embedding_vars = global_vars
    with _initialized_session():
        self.assertAllEqual(embedding_values, shared_embedding_vars[0])
        self.assertAllEqual(expected_lookups, self.evaluate(input_layer))
