# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
string_fc = fc._categorical_column_with_hash_bucket(
    'a_string', 10, dtype=dtypes.string)
int_fc = fc._categorical_column_with_hash_bucket(
    'a_int', 10, dtype=dtypes.int32)
float_fc = fc._categorical_column_with_hash_bucket(
    'a_float', 10, dtype=dtypes.string)
int_tensor = sparse_tensor.SparseTensor(
    values=[101],
    indices=[[0, 0]],
    dense_shape=[1, 1])
string_tensor = sparse_tensor.SparseTensor(
    values=['101'],
    indices=[[0, 0]],
    dense_shape=[1, 1])
float_tensor = sparse_tensor.SparseTensor(
    values=[101.],
    indices=[[0, 0]],
    dense_shape=[1, 1])
builder = _LazyBuilder({
    'a_int': int_tensor,
    'a_string': string_tensor,
    'a_float': float_tensor
})
builder.get(string_fc)
builder.get(int_fc)
with self.assertRaisesRegex(ValueError, 'dtype must be string or integer'):
    builder.get(float_fc)
