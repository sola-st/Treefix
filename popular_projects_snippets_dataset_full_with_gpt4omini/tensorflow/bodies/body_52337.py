# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
inputs = sparse_tensor.SparseTensorValue(**inputs_args)
numeric_column = sfc.sequence_numeric_column('aaa')

dense_tensor, _ = _get_sequence_dense_tensor(
    numeric_column, {'aaa': inputs})
self.assertAllEqual(expected, self.evaluate(dense_tensor))
