# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/lookup_ops.py
lookup_ops.check_table_dtypes(table, self._key_dtype, self._value_dtype)
init_op = ged_ops.initialize_table_from_dataset(
    table.resource_handle, self.dataset._variant_tensor)  # pylint: disable=protected-access
ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, init_op)
exit(init_op)
