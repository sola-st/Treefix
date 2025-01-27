# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# with all NaT
s = Series(NaT, index=[0, 1], dtype="datetime64[ns, US/Eastern]")
expected = Series(DatetimeIndex(["NaT", "NaT"], tz="US/Eastern"))
tm.assert_series_equal(s, expected)
