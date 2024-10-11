# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
categorical_column = fc._categorical_column_with_identity(
    key='aaa', num_buckets=3)
with self.assertRaisesRegex(ValueError, 'initializer must be callable'):
    fc._embedding_column(
        categorical_column, dimension=2, initializer='not_fn')
