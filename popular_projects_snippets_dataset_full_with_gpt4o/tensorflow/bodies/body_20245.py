# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
# Inputs.
vocabulary_size = 3
sparse_input = sparse_tensor.SparseTensorValue(
    # example 0, ids [2]
    # example 1, ids [0, 1]
    # example 2, ids []
    # example 3, ids [1]
    indices=((0, 0), (1, 0), (1, 1), (3, 0)),
    values=(2, 0, 1, 1),
    dense_shape=(4, 2))

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
expected_lookups_sequence = (
    # example 0, ids [2], embedding = [[7, 11], [0, 0]]
    ((7., 11.), (0., 0.),),
    # example 1, ids [0, 1], embedding = [[1, 2], [3. 5]]
    ((1., 2.), (3., 5.),),
    # example 2, ids [], embedding = [0, 0]
    ((0., 0.), (0., 0.),),
    # example 3, ids [1], embedding = [3, 5]
    ((3., 5.), (0., 0.),),
)

# Build columns.
categorical_column = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
sequence_categorical_column = (
    fc_lib.sequence_categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size))
embedding_column = tpu_fc.embedding_column_v2(
    categorical_column,
    dimension=embedding_dimension,
    initializer=_initializer,
    use_safe_embedding_lookup=use_safe_embedding_lookup)
sequence_embedding_column = tpu_fc.embedding_column_v2(
    sequence_categorical_column,
    dimension=embedding_dimension,
    initializer=_initializer,
    max_sequence_length=2,
    use_safe_embedding_lookup=use_safe_embedding_lookup)

# Provide sparse input and get dense result.
features = {'aaa': sparse_input, 'bbb': sparse_input}
dense_features = df_lib.DenseFeatures([embedding_column])
sequence_features = sfc_lib.SequenceFeatures([sequence_embedding_column])
embedding_lookup = dense_features(features)
sequence_embedding_lookup = sequence_features(features)

# Assert expected embedding variable and lookups.
global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
self.assertItemsEqual(
    ('dense_features/aaa_embedding/embedding_weights:0',
     'sequence_features/bbb_embedding/embedding_weights:0',),
    tuple([v.name for v in global_vars]))
with _initialized_session():
    self.assertAllEqual(embedding_values, global_vars[0])
    self.assertAllEqual(expected_lookups, embedding_lookup)
    self.assertAllEqual(expected_lookups_sequence,
                        sequence_embedding_lookup[0].eval())
    # The graph will still have SparseFillEmptyRows due to sequence being
    # a Rank3 embedding lookup.
    if use_safe_embedding_lookup:
        self.assertEqual(2, [
            x.type for x in ops.get_default_graph().get_operations()
        ].count('SparseFillEmptyRows'))
    else:
        self.assertEqual(1, [
            x.type for x in ops.get_default_graph().get_operations()
        ].count('SparseFillEmptyRows'))
