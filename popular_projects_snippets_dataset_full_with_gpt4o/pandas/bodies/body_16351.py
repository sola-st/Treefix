# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
s = Series([Timestamp("20130101"), Timestamp("20130101", tz="US/Eastern")])
expected = Series(
    [Timestamp("20130101"), Timestamp("20130101", tz="US/Eastern")],
    dtype="object",
)
tm.assert_series_equal(s, expected)
