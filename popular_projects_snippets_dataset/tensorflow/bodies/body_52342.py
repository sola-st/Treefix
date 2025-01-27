# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests _sequence_length when some examples do not have ids."""
sparse_input = sparse_tensor.SparseTensorValue(
    # example 0, values []
    # example 1, values [[0.], [1.]]
    # example 2, [[2.]]
    # example 3, values []
    # example 4, [[3.]]
    # example 5, values []
    indices=((1, 0), (1, 1), (2, 0), (4, 0)),
    values=(0., 1., 2., 3.),
    dense_shape=(6, 2))
expected_sequence_length = [0, 2, 1, 0, 1, 0]
numeric_column = sfc.sequence_numeric_column('aaa')

_, sequence_length = _get_sequence_dense_tensor(
    numeric_column, {'aaa': sparse_input})

self.assertAllEqual(
    expected_sequence_length, self.evaluate(sequence_length))
