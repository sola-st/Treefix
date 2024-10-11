# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# this is only locale tested with US/None locales
# GH 5195, GH50251
# with a format and coerce a single item to_datetime fails
td = Series(["May 04", "Jun 02", ""], index=[1, 2, 3])
expected = to_datetime(td, format="%b %y", errors=errors, cache=cache)

result = td.apply(
    lambda x: to_datetime(x, format="%b %y", errors="coerce", cache=cache)
)
tm.assert_series_equal(result, expected)
