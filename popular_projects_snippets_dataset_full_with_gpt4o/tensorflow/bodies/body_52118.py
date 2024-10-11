# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
# Inputs.
batch_size = 4
vocabulary_size = 3
sparse_input = sparse_tensor.SparseTensorValue(
    # example 0, ids [2]
    # example 1, ids [0, 1]
    # example 2, ids []
    # example 3, ids [1]
    indices=((0, 0), (1, 0), (1, 4), (3, 0)),
    values=(2, 0, 1, 1),
    dense_shape=(batch_size, 5))

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
categorical_column = fc._categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
embedding_column = fc._embedding_column(
    categorical_column,
    dimension=embedding_dimension,
    initializer=_initializer)

with ops.Graph().as_default():
    predictions = get_keras_linear_model_predictions({
        categorical_column.name: sparse_input
    }, (embedding_column,))
    expected_var_names = (
        'linear_model/bias_weights:0',
        'linear_model/aaa_embedding/weights:0',
        'linear_model/aaa_embedding/embedding_weights:0',
    )
    self.assertCountEqual(
        expected_var_names,
        [v.name for v in ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)])
    trainable_vars = {
        v.name: v
        for v in ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    }
    self.assertCountEqual(expected_var_names, trainable_vars.keys())
    bias = trainable_vars['linear_model/bias_weights:0']
    embedding_weights = trainable_vars[
        'linear_model/aaa_embedding/embedding_weights:0']
    linear_weights = trainable_vars['linear_model/aaa_embedding/weights:0']
    with _initialized_session():
        # Predictions with all zero weights.
        self.assertAllClose(np.zeros((1,)), self.evaluate(bias))
        self.assertAllClose(zeros_embedding_values,
                            self.evaluate(embedding_weights))
        self.assertAllClose(
            np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights))
        self.assertAllClose(
            np.zeros((batch_size, 1)), self.evaluate(predictions))

        # Predictions with all non-zero weights.
        embedding_weights.assign((
            (1., 2.),  # id 0
            (3., 5.),  # id 1
            (7., 11.)  # id 2
        )).eval()
        linear_weights.assign(((4.,), (6.,))).eval()
        # example 0, ids [2], embedding[0] = [7, 11]
        # example 1, ids [0, 1], embedding[1] = mean([1, 2] + [3, 5]) = [2, 3.5]
        # example 2, ids [], embedding[2] = [0, 0]
        # example 3, ids [1], embedding[3] = [3, 5]
        # sum(embeddings * linear_weights)
        # = [4*7 + 6*11, 4*2 + 6*3.5, 4*0 + 6*0, 4*3 + 6*5] = [94, 29, 0, 42]
        self.assertAllClose(((94.,), (29.,), (0.,), (42.,)),
                            self.evaluate(predictions))
