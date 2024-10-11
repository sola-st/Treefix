# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
hashed_sparse = fc._categorical_column_with_hash_bucket(
    'wire', 10, dtype=dtypes.int64)
wire_tensor = sparse_tensor.SparseTensor(
    values=['omar'], indices=[[0, 0]], dense_shape=[1, 1])
builder = _LazyBuilder({'wire': wire_tensor})
with self.assertRaisesRegex(ValueError, 'dtype must be compatible'):
    builder.get(hashed_sparse)
