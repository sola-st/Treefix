# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_rendering.py
# This can cause the tz field to be populated, but it's redundant to
# include this information in the date-string.
date_with_utc_offset = Timestamp("2014-03-13 00:00:00-0400", tz=None)
assert "2014-03-13 00:00:00-0400" in repr(date_with_utc_offset)
assert "tzoffset" not in repr(date_with_utc_offset)
assert "UTC-04:00" in repr(date_with_utc_offset)
expr = repr(date_with_utc_offset)
assert date_with_utc_offset == eval(expr)
