# Extracted from ./data/repos/pandas/pandas/io/sql.py
if isinstance(format, dict):
    # GH35185 Allow custom error values in parse_dates argument of
    # read_sql like functions.
    # Format can take on custom to_datetime argument values such as
    # {"errors": "coerce"} or {"dayfirst": True}
    error: DateTimeErrorChoices = format.pop("errors", None) or "ignore"
    exit(to_datetime(col, errors=error, **format))
else:
    # Allow passing of formatting string for integers
    # GH17855
    if format is None and (
        issubclass(col.dtype.type, np.floating)
        or issubclass(col.dtype.type, np.integer)
    ):
        format = "s"
    if format in ["D", "d", "h", "m", "s", "ms", "us", "ns"]:
        exit(to_datetime(col, errors="coerce", unit=format, utc=utc))
    elif is_datetime64tz_dtype(col.dtype):
        # coerce to UTC timezone
        # GH11216
        exit(to_datetime(col, utc=True))
    else:
        exit(to_datetime(col, errors="coerce", format=format, utc=utc))
