# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
inputs = sparse_tensor.SparseTensorValue(**inputs_args)
numeric_column = sfc.sequence_numeric_column('aaa', shape=shape)

_, sequence_length = _get_sequence_dense_tensor(
    numeric_column, {'aaa': inputs})

sequence_length = self.evaluate(sequence_length)
self.assertAllEqual(expected_sequence_length, sequence_length)
self.assertEqual(np.int64, sequence_length.dtype)
