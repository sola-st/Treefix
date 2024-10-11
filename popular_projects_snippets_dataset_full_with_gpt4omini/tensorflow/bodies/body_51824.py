# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
hashed_sparse = fc._categorical_column_with_hash_bucket('wire', 10)
wire_tensor = sparse_tensor.SparseTensor(
    values=['omar', 'stringer', 'marlo'],
    indices=[[0, 0], [1, 0], [1, 1]],
    dense_shape=[2, 2])
outputs = _transform_features({'wire': wire_tensor}, [hashed_sparse])
output = outputs[hashed_sparse]
# Check exact hashed output. If hashing changes this test will break.
expected_values = [6, 4, 1]
with self.cached_session():
    self.assertEqual(dtypes.int64, output.values.dtype)
    self.assertAllEqual(expected_values, output.values)
    self.assertAllEqual(wire_tensor.indices, output.indices)
    self.assertAllEqual(wire_tensor.dense_shape, output.dense_shape)
