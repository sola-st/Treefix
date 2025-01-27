# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests _sequence_length when some examples do not have ids."""
vocabulary_size = 3
sparse_input = sparse_tensor.SparseTensorValue(
    # example 0, ids []
    # example 1, ids [2]
    # example 2, ids [0, 1]
    # example 3, ids []
    # example 4, ids [1]
    # example 5, ids []
    indices=((1, 0), (2, 0), (2, 1), (4, 0)),
    values=(2, 0, 1, 1),
    dense_shape=(6, 2))
expected_sequence_length = [0, 1, 2, 0, 1, 0]

categorical_column = sfc.sequence_categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
indicator_column = fc.indicator_column(categorical_column)

_, sequence_length = _get_sequence_dense_tensor(
    indicator_column, {'aaa': sparse_input})

self.assertAllEqual(
    expected_sequence_length, self.evaluate(sequence_length))
