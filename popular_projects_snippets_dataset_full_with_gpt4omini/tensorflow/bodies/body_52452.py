# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
hashed_sparse = fc.categorical_column_with_hash_bucket('wire', 10)
wire_tensor = sparse_tensor.SparseTensor(
    values=['omar', 'stringer', 'marlo'],
    indices=[[0, 0], [1, 0], [1, 1]],
    dense_shape=[2, 2])
outputs = fc._transform_features_v2({
    'wire': wire_tensor
}, [hashed_sparse], None)
output = outputs[hashed_sparse]
# Check exact hashed output. If hashing changes this test will break.
expected_values = [6, 4, 1]

self.assertEqual(dtypes.int64, output.values.dtype)
self.assertAllEqual(expected_values, self.evaluate(output.values))
self.assertAllEqual(
    self.evaluate(wire_tensor.indices), self.evaluate(output.indices))
self.assertAllEqual(
    self.evaluate(wire_tensor.dense_shape),
    self.evaluate(output.dense_shape))
