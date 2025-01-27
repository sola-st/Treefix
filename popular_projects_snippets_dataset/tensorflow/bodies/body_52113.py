# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
# Inputs.
vocabulary_size = 3
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
    (7., 11.)  # id 2
)
def _initializer(shape, dtype, partition_info):
    self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
    self.assertEqual(dtypes.float32, dtype)
    self.assertIsNone(partition_info)
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
embedding_column = fc._embedding_column(
    categorical_column,
    dimension=embedding_dimension,
    initializer=_initializer)

# Provide sparse input and get dense result.
input_indices = array_ops.placeholder(dtype=dtypes.int64)
input_values = array_ops.placeholder(dtype=dtypes.int64)
input_shape = array_ops.placeholder(dtype=dtypes.int64)
embedding_lookup = embedding_column._get_dense_tensor(
    _LazyBuilder({
        'aaa':
            sparse_tensor.SparseTensorValue(
                indices=input_indices,
                values=input_values,
                dense_shape=input_shape)
    }))

# Assert expected embedding variable and lookups.
global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
self.assertCountEqual(('embedding_weights:0',),
                      tuple([v.name for v in global_vars]))
with _initialized_session():
    self.assertAllEqual(embedding_values, global_vars[0])
    self.assertAllEqual(expected_lookups, embedding_lookup.eval(
        feed_dict={
            input_indices: sparse_input.indices,
            input_values: sparse_input.values,
            input_shape: sparse_input.dense_shape,
        }))
