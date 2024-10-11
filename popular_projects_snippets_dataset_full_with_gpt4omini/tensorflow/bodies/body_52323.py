# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
inputs = sparse_tensor.SparseTensorValue(**inputs_args)
vocabulary_size = 3

categorical_column = sfc.sequence_categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
embedding_column = fc.embedding_column(
    categorical_column, dimension=2)

_, sequence_length, _ = _get_sequence_dense_tensor_state(
    embedding_column, {'aaa': inputs})

sequence_length = self.evaluate(sequence_length)
self.assertAllEqual(expected_sequence_length, sequence_length)
self.assertEqual(np.int64, sequence_length.dtype)
