# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
hashed_sparse = fc._categorical_column_with_hash_bucket(
    'wire', 10, dtype=dtypes.int64)
wire_tensor = sparse_tensor.SparseTensor(
    values=[101, 201, 301],
    indices=[[0, 0], [1, 0], [1, 1]],
    dense_shape=[2, 2])
builder = _LazyBuilder({'wire': wire_tensor})
output = builder.get(hashed_sparse)
# Check exact hashed output. If hashing changes this test will break.
expected_values = [3, 7, 5]
with self.cached_session():
    self.assertAllEqual(expected_values, output.values)
