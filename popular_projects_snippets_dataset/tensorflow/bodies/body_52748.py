# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    def _initializer(shape, dtype, partition_info=None):
        del shape, dtype, partition_info
        exit(ValueError('Not expected to be called'))

    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=3)
    embedding_column_a, embedding_column_b = fc.shared_embedding_columns_v2(
        [categorical_column_a, categorical_column_b],
        dimension=2,
        initializer=_initializer)

    self.assertEqual([categorical_column_a], embedding_column_a.parents)
    self.assertEqual([categorical_column_b], embedding_column_b.parents)
    # TODO(rohanj): Add tests for (from|get)_config once implemented
