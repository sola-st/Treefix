# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
hashed_sparse = fc.categorical_column_with_hash_bucket(
    'wire', 10, dtype=dtypes.int64)
wire_tensor = sparse_tensor.SparseTensor(
    values=[101, 201, 301],
    indices=[[0, 0], [1, 0], [1, 1]],
    dense_shape=[2, 2])
transformation_cache = fc.FeatureTransformationCache({'wire': wire_tensor})
output = transformation_cache.get(hashed_sparse, None)
# Check exact hashed output. If hashing changes this test will break.
expected_values = [3, 7, 5]

self.assertAllEqual(expected_values, self.evaluate(output.values))
