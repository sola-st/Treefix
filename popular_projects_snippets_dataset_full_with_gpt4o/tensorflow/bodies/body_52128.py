# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=3)
    weighted_categorical_column_a = fc._weighted_categorical_column(
        categorical_column_a, weight_feature_key='aaa_weights')
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=3)
    weighted_categorical_column_b = fc._weighted_categorical_column(
        categorical_column_b, weight_feature_key='bbb_weights')
    fc_new.shared_embedding_columns(
        [weighted_categorical_column_a, categorical_column_b], dimension=2)
    fc_new.shared_embedding_columns(
        [categorical_column_a, weighted_categorical_column_b], dimension=2)
    fc_new.shared_embedding_columns(
        [weighted_categorical_column_a, weighted_categorical_column_b],
        dimension=2)
