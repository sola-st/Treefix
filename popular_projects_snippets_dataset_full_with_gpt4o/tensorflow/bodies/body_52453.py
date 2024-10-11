# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
string_fc = fc.categorical_column_with_hash_bucket(
    'a_string', 10, dtype=dtypes.string)
int_fc = fc.categorical_column_with_hash_bucket(
    'a_int', 10, dtype=dtypes.int32)
float_fc = fc.categorical_column_with_hash_bucket(
    'a_float', 10, dtype=dtypes.string)
int_tensor = sparse_tensor.SparseTensor(
    values=[101], indices=[[0, 0]], dense_shape=[1, 1])
string_tensor = sparse_tensor.SparseTensor(
    values=['101'], indices=[[0, 0]], dense_shape=[1, 1])
float_tensor = sparse_tensor.SparseTensor(
    values=[101.], indices=[[0, 0]], dense_shape=[1, 1])
transformation_cache = fc.FeatureTransformationCache({
    'a_int': int_tensor,
    'a_string': string_tensor,
    'a_float': float_tensor
})
transformation_cache.get(string_fc, None)
transformation_cache.get(int_fc, None)
with self.assertRaisesRegex(ValueError, 'dtype must be string or integer'):
    transformation_cache.get(float_fc, None)
