# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
categorical_column = fc.categorical_column_with_identity(
    key='aaa', num_buckets=3)
with self.assertRaisesRegex(ValueError, 'initializer must be callable'):
    fc.embedding_column(categorical_column, dimension=2, initializer='not_fn')
