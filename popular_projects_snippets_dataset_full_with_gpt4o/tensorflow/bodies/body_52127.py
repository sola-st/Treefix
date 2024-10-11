# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=3)
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=3)
    categorical_column_c = fc._categorical_column_with_hash_bucket(
        key='ccc', hash_bucket_size=3)
    with self.assertRaisesRegex(
        ValueError, 'all categorical_columns must have the same type.*'
        '_IdentityCategoricalColumn.*_HashedCategoricalColumn'):
        fc_new.shared_embedding_columns(
            [categorical_column_a, categorical_column_b, categorical_column_c],
            dimension=2)
