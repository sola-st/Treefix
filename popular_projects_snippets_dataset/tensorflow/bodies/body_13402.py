# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Check that the given key_dtype and value_dtype matches the table dtypes.

  Args:
    table: The table to check types against to.
    key_dtype: The key data type to check.
    value_dtype: The value data type to check.

  Raises:
    TypeError: when 'key_dtype' or 'value_dtype' doesn't match the table data
      types.
  """
if key_dtype.base_dtype != table.key_dtype:
    raise TypeError(f"Invalid key dtype for table, expected {table.key_dtype} "
                    f"but got {key_dtype}.")
if value_dtype.base_dtype != table.value_dtype:
    raise TypeError("Invalid value dtype for table, expected "
                    f"{table.value_dtype} but got {value_dtype}.")
