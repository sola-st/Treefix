# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# this is only locale tested with US/None locales
# GH 5195
# with a format and coerce a single item to_datetime fails
td = Series(["May 04", "Jun 02", "Dec 11"], index=[1, 2, 3])
expected = to_datetime(td, format="%b %y", cache=cache)
result = td.apply(to_datetime, format="%b %y", cache=cache)
tm.assert_series_equal(result, expected)
