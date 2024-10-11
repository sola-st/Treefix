# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    # Inputs.
    batch_size = 2
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

    # Embedding variable.
    embedding_dimension = 2
    embedding_shape = (vocabulary_size, embedding_dimension)
    zeros_embedding_values = np.zeros(embedding_shape)

    def _initializer(shape, dtype, partition_info):
        self.assertAllEqual(embedding_shape, shape)
        self.assertEqual(dtypes.float32, dtype)
        self.assertIsNone(partition_info)
        exit(zeros_embedding_values)

    # Build columns.
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)
    embedding_column_a, embedding_column_b = fc_new.shared_embedding_columns(
        [categorical_column_a, categorical_column_b],
        dimension=embedding_dimension,
        initializer=_initializer)

    predictions = fc.linear_model({
        categorical_column_a.name: input_a,
        categorical_column_b.name: input_b,
    }, (embedding_column_a, embedding_column_b))
    # Linear weights do not follow the column name. But this is a rare use
    # case, and fixing it would add too much complexity to the code.
    expected_var_names = (
        'linear_model/bias_weights:0',
        'linear_model/aaa_bbb_shared_embedding/weights:0',
        'linear_model/aaa_bbb_shared_embedding/embedding_weights:0',
        'linear_model/aaa_bbb_shared_embedding_1/weights:0',
    )
    self.assertCountEqual(
        expected_var_names,
        [v.name for v in ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)])
    trainable_vars = {
        v.name: v for v in ops.get_collection(
            ops.GraphKeys.TRAINABLE_VARIABLES)
    }
    self.assertCountEqual(expected_var_names, trainable_vars.keys())
    bias = trainable_vars['linear_model/bias_weights:0']
    embedding_weights = trainable_vars[
        'linear_model/aaa_bbb_shared_embedding/embedding_weights:0']
    linear_weights_a = trainable_vars[
        'linear_model/aaa_bbb_shared_embedding/weights:0']
    linear_weights_b = trainable_vars[
        'linear_model/aaa_bbb_shared_embedding_1/weights:0']
    with _initialized_session():
        # Predictions with all zero weights.
        self.assertAllClose(np.zeros((1,)), self.evaluate(bias))
        self.assertAllClose(zeros_embedding_values,
                            self.evaluate(embedding_weights))
        self.assertAllClose(
            np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights_a))
        self.assertAllClose(
            np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights_b))
        self.assertAllClose(
            np.zeros((batch_size, 1)), self.evaluate(predictions))

        # Predictions with all non-zero weights.
        embedding_weights.assign((
            (1., 2.),  # id 0
            (3., 5.),  # id 1
            (7., 11.)  # id 2
        )).eval()
        linear_weights_a.assign(((4.,), (6.,))).eval()
        # example 0, ids [2], embedding[0] = [7, 11]
        # example 1, ids [0, 1], embedding[1] = mean([1, 2] + [3, 5]) = [2, 3.5]
        # sum(embeddings * linear_weights)
        # = [4*7 + 6*11, 4*2 + 6*3.5] = [94, 29]
        linear_weights_b.assign(((3.,), (5.,))).eval()
        # example 0, ids [0], embedding[0] = [1, 2]
        # example 1, ids [], embedding[1] = 0, 0]
        # sum(embeddings * linear_weights)
        # = [3*1 + 5*2, 3*0 +5*0] = [13, 0]
        self.assertAllClose([[94. + 13.], [29.]], self.evaluate(predictions))
