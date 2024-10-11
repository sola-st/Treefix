# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
vocabulary_size = 3
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

with ops.Graph().as_default():
    sparse_input_a = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 1), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 2))
    sparse_input_b = sparse_tensor.SparseTensorValue(
        # example 0, ids [1]
        # example 1, ids [0, 2]
        # example 2, ids [0]
        # example 3, ids []
        indices=((0, 0), (1, 0), (1, 1), (2, 0)),
        values=(1, 0, 2, 0),
        dense_shape=(4, 2))

    expected_lookups_a = [
        # example 0, ids [2]
        [[7., 11.], [0., 0.]],
        # example 1, ids [0, 1]
        [[1., 2.], [3., 5.]],
        # example 2, ids []
        [[0., 0.], [0., 0.]],
        # example 3, ids [1]
        [[3., 5.], [0., 0.]],
    ]

    expected_lookups_b = [
        # example 0, ids [1]
        [[3., 5.], [0., 0.]],
        # example 1, ids [0, 2]
        [[1., 2.], [7., 11.]],
        # example 2, ids [0]
        [[1., 2.], [0., 0.]],
        # example 3, ids []
        [[0., 0.], [0., 0.]],
    ]

    categorical_column_a = sfc.sequence_categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = sfc.sequence_categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)
    shared_embedding_columns = fc.shared_embedding_columns_v2(
        [categorical_column_a, categorical_column_b],
        dimension=embedding_dimension,
        initializer=_initializer)

    embedding_lookup_a = _get_sequence_dense_tensor(
        shared_embedding_columns[0], {'aaa': sparse_input_a})[0]
    embedding_lookup_b = _get_sequence_dense_tensor(
        shared_embedding_columns[1], {'bbb': sparse_input_b})[0]

    self.evaluate(variables_lib.global_variables_initializer())
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('aaa_bbb_shared_embedding:0',),
                          tuple([v.name for v in global_vars]))
    self.assertAllEqual(embedding_values, self.evaluate(global_vars[0]))
    self.assertAllEqual(
        expected_lookups_a, self.evaluate(embedding_lookup_a))
    self.assertAllEqual(expected_lookups_b, self.evaluate(embedding_lookup_b))
