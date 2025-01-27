# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests _sequence_length when some examples do not have ids."""
with ops.Graph().as_default():
    vocabulary_size = 3
    sparse_input_a = sparse_tensor.SparseTensorValue(
        # example 0, ids []
        # example 1, ids [2]
        # example 2, ids [0, 1]
        # example 3, ids []
        # example 4, ids [1]
        # example 5, ids []
        indices=((1, 0), (2, 0), (2, 1), (4, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(6, 2))
    expected_sequence_length_a = [0, 1, 2, 0, 1, 0]
    categorical_column_a = sfc.sequence_categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)

    sparse_input_b = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids []
        # example 2, ids []
        # example 3, ids []
        # example 4, ids [1]
        # example 5, ids [0, 1]
        indices=((0, 0), (4, 0), (5, 0), (5, 1)),
        values=(2, 1, 0, 1),
        dense_shape=(6, 2))
    expected_sequence_length_b = [1, 0, 0, 0, 1, 2]
    categorical_column_b = sfc.sequence_categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)

    shared_embedding_columns = fc.shared_embedding_columns_v2(
        [categorical_column_a, categorical_column_b], dimension=2)

    sequence_length_a = _get_sequence_dense_tensor(
        shared_embedding_columns[0], {'aaa': sparse_input_a})[1]
    sequence_length_b = _get_sequence_dense_tensor(
        shared_embedding_columns[1], {'bbb': sparse_input_b})[1]

    with _initialized_session() as sess:
        self.assertAllEqual(
            expected_sequence_length_a, sequence_length_a.eval(session=sess))
        self.assertAllEqual(
            expected_sequence_length_b, sequence_length_b.eval(session=sess))
