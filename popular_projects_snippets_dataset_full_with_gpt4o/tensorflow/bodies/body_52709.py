# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
categorical_column = fc_old._categorical_column_with_identity(
    key='aaa', num_buckets=3)
embedding_dimension = 2
embedding_column = fc.embedding_column(
    categorical_column, dimension=embedding_dimension)
self.assertFalse(embedding_column._is_v2_column)
