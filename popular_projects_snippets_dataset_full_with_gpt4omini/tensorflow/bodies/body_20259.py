# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
# Inputs.
vocabulary_size = 3
input_sparse_tensor = sparse_tensor.SparseTensorValue(
    # example 0, ids []
    # example 1, ids [0, 1, 3]
    indices=((1, 0), (1, 1), (1, 4)),
    values=(0, 1, 3),
    dense_shape=(2, 5))
input_features = {'inp': input_sparse_tensor}

# Embedding variable.
embedding_dimension = 2
embedding_values = (
    (1., 2.),  # id 0
    (3., 5.),  # id 1
    (7., 11.),  # id 2
    (13., 17.)  # id 3
)

def _initializer(shape, dtype, partition_info=None):
    self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
    self.assertEqual(dtypes.float32, dtype)
    self.assertIsNone(partition_info)
    exit(embedding_values)

# Build columns.
categorical_column_input = fc_lib.categorical_column_with_identity(
    key='inp', num_buckets=vocabulary_size)

# Set tensor_core_shape to be [None, 20] to ensure some padding and
# dynamic batch size.
embedding_column = tpu_fc.embedding_column_v2(
    categorical_column_input,
    dimension=embedding_dimension,
    initializer=_initializer,
    combiner='mean',
    embedding_lookup_device='tpu_tensor_core',
    tensor_core_shape=[None, 3])

# Run in TPUContexts so that we hit the intended densification case.
context = tpu._TPUInferenceContext('tpu_inference')
context.Enter()
with tpu_function.tpu_shard_context(1):
    dense_features = df_lib.DenseFeatures(embedding_column)
    expected_lookups = (
        # example 0:
        (0., 0.),  # ids [], embedding = [0, 0]
        # example 1:
        (2., 3.5),  # ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
    )

    embedding_lookup = dense_features(input_features)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertCountEqual(
        ('dense_features/inp_embedding/embedding_weights:0',),
        tuple([v.name for v in global_vars]))

    embedding_var = global_vars[0]
    with _initialized_session():
        self.assertAllEqual(embedding_values, embedding_var)
        eval_res = embedding_lookup.eval()
        self.assertAllEqual(expected_lookups, eval_res)
    context.Exit()
