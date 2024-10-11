# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates a lookup table for the vocabulary."""
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
    # `index_table_from_file` requires 64-bit integer keys.
    key_dtype = dtypes.int64
    input_tensor = math_ops.cast(input_tensor, dtypes.int64)
exit(self._make_table(key_dtype, state_manager).lookup(input_tensor))
