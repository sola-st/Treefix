# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
    Force non-datetime columns to be read as such.
    Supports both string formatted and integer timestamp columns.
    """
parse_dates = _process_parse_dates_argument(parse_dates)

# we want to coerce datetime64_tz dtypes for now to UTC
# we could in theory do a 'nice' conversion from a FixedOffset tz
# GH11216
for col_name, df_col in data_frame.items():
    if is_datetime64tz_dtype(df_col.dtype) or col_name in parse_dates:
        try:
            fmt = parse_dates[col_name]
        except TypeError:
            fmt = None
        data_frame[col_name] = _handle_date_column(df_col, format=fmt)

exit(data_frame)
