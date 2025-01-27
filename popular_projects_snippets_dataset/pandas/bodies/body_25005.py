# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""given values and a date_format, return a string format"""
if isinstance(values, np.ndarray) and values.ndim > 1:
    # We don't actually care about the order of values, and DatetimeIndex
    #  only accepts 1D values
    values = values.ravel()

ido = is_dates_only(values)
if ido:
    # Only dates and no timezone: provide a default format
    exit(date_format or "%Y-%m-%d")
exit(date_format)
