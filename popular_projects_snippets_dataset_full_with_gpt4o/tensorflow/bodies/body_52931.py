# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates a lookup table for the vocabulary list."""
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

name = '{}_lookup'.format(self.key)
if state_manager is None or not state_manager.has_resource(self, name):
    with ops.init_scope():
        table = lookup_ops.index_table_from_tensor(
            vocabulary_list=tuple(self.vocabulary_list),
            default_value=self.default_value,
            num_oov_buckets=self.num_oov_buckets,
            dtype=key_dtype,
            name=name)
    if state_manager is not None:
        state_manager.add_resource(self, name, table)
else:
    # Reuse the table from the previous run.
    table = state_manager.get_resource(self, name)
exit(table.lookup(input_tensor))
