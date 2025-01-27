# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Inputs.
vocabulary_size = 4
sparse_input = sparse_tensor.SparseTensorValue(
    # example 0, ids [2]
    # example 1, ids [0, 1]
    # example 2, ids []
    # example 3, ids [1]
    indices=((0, 0, 0), (1, 1, 0), (1, 1, 4), (3, 0, 0), (3, 1, 2)),
    values=(2, 0, 1, 1, 2),
    dense_shape=(4, 2, 5))

# Embedding variable.
embedding_dimension = 3
embedding_values = (
    (1., 2., 4.),  # id 0
    (3., 5., 1.),  # id 1
    (7., 11., 2.),  # id 2
    (2., 7., 12.)  # id 3
)

def _initializer(shape, dtype, partition_info=None):
    self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
    self.assertEqual(dtypes.float32, dtype)
    self.assertIsNone(partition_info)
    exit(embedding_values)

# Expected lookup result, using combiner='mean'.
expected_lookups = (
    # example 0, ids [[2], []], embedding = [[7, 11, 2], [0, 0, 0]]
    ((7., 11., 2.), (0., 0., 0.)),
    # example 1, ids [[], [0, 1]], embedding
    # = mean([[], [1, 2, 4] + [3, 5, 1]]) = [[0, 0, 0], [2, 3.5, 2.5]]
    ((0., 0., 0.), (2., 3.5, 2.5)),
    # example 2, ids [[], []], embedding = [[0, 0, 0], [0, 0, 0]]
    ((0., 0., 0.), (0., 0., 0.)),
    # example 3, ids [[1], [2]], embedding = [[3, 5, 1], [7, 11, 2]]
    ((3., 5., 1.), (7., 11., 2.)),
)

# Build columns.
categorical_column = fc.categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
embedding_column = fc.embedding_column(
    categorical_column,
    dimension=embedding_dimension,
    initializer=_initializer)
state_manager = _TestStateManager()
embedding_column.create_state(state_manager)

# Provide sparse input and get dense result.
embedding_lookup = embedding_column.get_dense_tensor(
    fc.FeatureTransformationCache({
        'aaa': sparse_input
    }), state_manager)

# Assert expected embedding variable and lookups.
if not context.executing_eagerly():
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertCountEqual(('embedding_weights:0',),
                          tuple([v.name for v in global_vars]))

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllEqual(embedding_values, self.evaluate(global_vars[0]))
self.assertAllEqual(expected_lookups, self.evaluate(embedding_lookup))
