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

# Embedding variable. The checkpoint file contains _embedding_values.
embedding_dimension = 2
embedding_values = (
    (1., 2.),  # id 0
    (3., 5.),  # id 1
    (7., 11.)  # id 2
)
ckpt_path = test.test_src_dir_path(
    'python/feature_column/testdata/embedding.ckpt')
ckpt_tensor = 'my_embedding'

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
    ckpt_to_load_from=ckpt_path,
    tensor_name_in_ckpt=ckpt_tensor)
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
