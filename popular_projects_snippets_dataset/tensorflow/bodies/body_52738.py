# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)
    weighted_categorical_column_a = fc.weighted_categorical_column(
        categorical_column_a, weight_feature_key='aaa_weights')
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=3)
    weighted_categorical_column_b = fc.weighted_categorical_column(
        categorical_column_b, weight_feature_key='bbb_weights')
    fc.shared_embedding_columns_v2(
        [weighted_categorical_column_a, categorical_column_b], dimension=2)
    fc.shared_embedding_columns_v2(
        [categorical_column_a, weighted_categorical_column_b], dimension=2)
    fc.shared_embedding_columns_v2(
        [weighted_categorical_column_a, weighted_categorical_column_b],
        dimension=2)
