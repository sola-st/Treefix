# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
vocabulary_size = 3
categorical_column_a = fc_lib.categorical_column_with_identity(
    key='aaa', num_buckets=vocabulary_size)
categorical_column_b = fc_lib.categorical_column_with_identity(
    key='bbb', num_buckets=vocabulary_size)
embedding_dimension = 2
columns = tpu_fc.shared_embedding_columns_v2(
    [categorical_column_b, categorical_column_a],
    dimension=embedding_dimension)
columns_copy = copy.deepcopy(columns)
self.assertEqual(
    [column._shared_embedding_collection_name for column in columns],
    [column._shared_embedding_collection_name for column in columns_copy])
