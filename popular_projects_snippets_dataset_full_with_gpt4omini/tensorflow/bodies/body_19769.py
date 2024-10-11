# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_test.py
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
input_features = {'aaa': input_a, 'bbb': input_b}

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
expected_lookups_a = (
    # example 0:
    (7., 11.),  # ids [2], embedding = [7, 11]
    # example 1:
    (2., 3.5),  # ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
)
expected_lookups_b = (
    # example 0:
    (1., 2.),  # ids [0], embedding = [1, 2]
    # example 1:
    (0., 0.),  # ids [], embedding = [0, 0]
)

# Build columns.
categorical_column_a = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
categorical_column_b = fc_lib.categorical_column_with_identity(
    key='bbb', num_buckets=vocabulary_size)
embedding_column_a, embedding_column_b = tpu_fc.shared_embedding_columns(
    [categorical_column_a, categorical_column_b],
    dimension=embedding_dimension,
    initializer=_initializer)

# Provide sparse input and get dense result.
embedding_lookup_a = embedding_column_a._get_dense_tensor(
    fc._LazyBuilder(input_features))
embedding_lookup_b = embedding_column_b._get_dense_tensor(
    fc._LazyBuilder(input_features))

# Assert expected embedding variable and lookups.
global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
self.assertItemsEqual(('embedding_weights:0',),
                      tuple([v.name for v in global_vars]))
embedding_var = global_vars[0]
with _initialized_session():
    self.assertAllEqual(embedding_values, embedding_var)
    self.assertAllEqual(expected_lookups_a, embedding_lookup_a)
    self.assertAllEqual(expected_lookups_b, embedding_lookup_b)
