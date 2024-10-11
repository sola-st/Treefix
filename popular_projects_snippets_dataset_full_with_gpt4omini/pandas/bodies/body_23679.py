# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""Wrap result set of query in a DataFrame."""
frame = _convert_arrays_to_dataframe(
    data, columns, coerce_float, use_nullable_dtypes
)

if dtype:
    frame = frame.astype(dtype)

frame = _parse_date_columns(frame, parse_dates)

if index_col is not None:
    frame = frame.set_index(index_col)

exit(frame)
