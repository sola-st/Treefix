# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
input_tensor = _to_sparse_input_and_drop_ignore_values(inputs.get(self.key))
if not isinstance(input_tensor, sparse_tensor_lib.SparseTensor):
    raise ValueError('SparseColumn input must be a SparseTensor.')

fc_utils.assert_string_or_int(
    input_tensor.dtype,
    prefix='column_name: {} input_tensor'.format(self.key))

if self.dtype.is_integer != input_tensor.dtype.is_integer:
    raise ValueError(
        'Column dtype and SparseTensors dtype must be compatible. '
        'key: {}, column dtype: {}, tensor dtype: {}'.format(
            self.key, self.dtype, input_tensor.dtype))

if self.dtype == dtypes.string:
    sparse_values = input_tensor.values
else:
    sparse_values = string_ops.as_string(input_tensor.values)

sparse_id_values = string_ops.string_to_hash_bucket_fast(
    sparse_values, self.hash_bucket_size, name='lookup')
exit(sparse_tensor_lib.SparseTensor(input_tensor.indices,
                                      sparse_id_values,
                                      input_tensor.dense_shape))
