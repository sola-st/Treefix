# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_test.py
# HashedCategoricalColumn is denylisted and so will raise an exception.
categorical_column = fc_lib.categorical_column_with_hash_bucket(
    key='aaa', hash_bucket_size=3)
embedding_dimension = 2
with self.assertRaises(TypeError):
    tpu_fc.embedding_column(categorical_column, dimension=embedding_dimension)
