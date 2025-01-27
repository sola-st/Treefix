# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
categorical_column = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_dimension = 2
initializer = init_ops.truncated_normal_initializer(mean=0.0, stddev=.5)
embedding_column = tpu_fc._TPUEmbeddingColumnV2(
    categorical_column=categorical_column,
    dimension=embedding_dimension,
    combiner='mean',
    initializer=initializer,
    max_sequence_length=0,
    use_safe_embedding_lookup=False,
    bypass_scope_validation=True)
embedding_column_copy = copy.deepcopy(embedding_column)
self.assertEqual(embedding_dimension, embedding_column_copy.dimension)
self.assertEqual(embedding_column._max_sequence_length,
                 embedding_column_copy._max_sequence_length)
self.assertTrue(embedding_column_copy._bypass_scope_validation)
self.assertFalse(embedding_column_copy.use_safe_embedding_lookup)
