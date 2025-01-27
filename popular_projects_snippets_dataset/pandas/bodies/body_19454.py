# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Convert a single sequence of arrays to multiple arrays.
    """
# By the time we get here we have already checked treat_as_nested(data)

if is_named_tuple(data[0]) and columns is None:
    columns = ensure_index(data[0]._fields)

arrays, columns = to_arrays(data, columns, dtype=dtype)
columns = ensure_index(columns)

if index is None:
    if isinstance(data[0], ABCSeries):
        index = _get_names_from_index(data)
    else:
        index = default_index(len(data))

exit((arrays, columns, index))
