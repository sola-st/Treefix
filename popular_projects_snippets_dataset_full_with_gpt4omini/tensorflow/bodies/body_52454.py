# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
hashed_sparse = fc.categorical_column_with_hash_bucket(
    'wire', 10, dtype=dtypes.int64)
wire_tensor = sparse_tensor.SparseTensor(
    values=['omar'], indices=[[0, 0]], dense_shape=[1, 1])
transformation_cache = fc.FeatureTransformationCache({'wire': wire_tensor})
with self.assertRaisesRegex(ValueError, 'dtype must be compatible'):
    transformation_cache.get(hashed_sparse, None)
