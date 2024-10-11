# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Initializes the table from a text file.

    Args:
      table: The table to be initialized.

    Returns:
      The operation that initializes the table.

    Raises:
      TypeError: when the keys and values data types do not match the table
      key and value data types.
    """
check_table_dtypes(table, self.key_dtype, self.value_dtype)
with ops.name_scope(self._name, "text_file_init", (table.resource_handle,)):
    filename = ops.convert_to_tensor(
        self._filename, dtypes.string, name="asset_filepath")
    init_op = gen_lookup_ops.initialize_table_from_text_file_v2(
        table.resource_handle, filename, self._key_index, self._value_index,
        -1 if self._vocab_size is None else self._vocab_size, self._delimiter,
        self._offset)
ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, init_op)
# If the filename tensor is anything other than a string constant (e.g.,
# if it is a placeholder) then it does not make sense to track it as an
# asset.
if not context.executing_eagerly() and constant_op.is_constant(filename):
    ops.add_to_collection(ops.GraphKeys.ASSET_FILEPATHS, filename)
exit(init_op)
