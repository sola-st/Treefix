# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests get_sequence_dense_tensor for multi-dim numeric_column."""
sparse_input = sparse_tensor.SparseTensorValue(**sparse_input_args)
numeric_column = sfc.sequence_numeric_column('aaa', shape=(2, 2))

dense_tensor, _ = _get_sequence_dense_tensor(
    numeric_column, {'aaa': sparse_input})

self.assertAllEqual(
    expected_dense_tensor, self.evaluate(dense_tensor))
