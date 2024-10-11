# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
categorical_column = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_column = tpu_fc.embedding_column_v2(
    categorical_column, dimension=2)
embedding_column_copy = copy.deepcopy(embedding_column)
self.assertEqual(embedding_column.dimension,
                 embedding_column_copy.dimension)
self.assertEqual(embedding_column._max_sequence_length,
                 embedding_column_copy._max_sequence_length)
