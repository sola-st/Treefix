# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
inputs = sparse_tensor.SparseTensorValue(**inputs_args)
vocabulary_size = 3

categorical_column = sfc.sequence_categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
indicator_column = fc.indicator_column(categorical_column)

indicator_tensor, _ = _get_sequence_dense_tensor(
    indicator_column, {'aaa': inputs})

self.assertAllEqual(expected, self.evaluate(indicator_tensor))
