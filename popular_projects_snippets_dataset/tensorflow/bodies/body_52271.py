# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
input_tensor = _to_sparse_input_and_drop_ignore_values(inputs.get(self.key))

if self.dtype.is_integer != input_tensor.dtype.is_integer:
    raise ValueError(
        'Column dtype and SparseTensors dtype must be compatible. '
        'key: {}, column dtype: {}, tensor dtype: {}'.format(
            self.key, self.dtype, input_tensor.dtype))

fc_utils.assert_string_or_int(
    input_tensor.dtype,
    prefix='column_name: {} input_tensor'.format(self.key))

key_dtype = self.dtype
if input_tensor.dtype.is_integer:
    # `index_table_from_tensor` requires 64-bit integer keys.
    key_dtype = dtypes.int64
    input_tensor = math_ops.cast(input_tensor, dtypes.int64)

exit(lookup_ops.index_table_from_tensor(
    vocabulary_list=tuple(self.vocabulary_list),
    default_value=self.default_value,
    num_oov_buckets=self.num_oov_buckets,
    dtype=key_dtype,
    name='{}_lookup'.format(self.key)).lookup(input_tensor))
