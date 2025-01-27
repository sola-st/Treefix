# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
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

def _initializer(shape, dtype, partition_info=None):
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
categorical_column = fc.categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
embedding_column = fc.embedding_column(
    categorical_column,
    dimension=embedding_dimension,
    initializer=_initializer)

# Provide sparse input and get dense result.
feature_layer = fc_old.input_layer({
    'aaa': sparse_input
}, (embedding_column,))

if not context.executing_eagerly():
    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertCountEqual(('input_layer/aaa_embedding/embedding_weights:0',),
                          tuple([v.name for v in global_vars]))
    trainable_vars = ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    self.assertCountEqual(('input_layer/aaa_embedding/embedding_weights:0',),
                          tuple([v.name for v in trainable_vars]))

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllEqual(embedding_values, self.evaluate(trainable_vars[0]))
self.assertAllEqual(expected_lookups, self.evaluate(feature_layer))
