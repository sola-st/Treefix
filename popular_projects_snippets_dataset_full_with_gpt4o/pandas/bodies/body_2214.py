# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 11871
ser = Series(["2014-1-1", "2014-2-2", "2015-3-3"])
expected = Series(
    [
        Timestamp("2014-01-01"),
        Timestamp("2014-02-02"),
        Timestamp("2015-03-03"),
    ]
)
tm.assert_series_equal(to_datetime(ser, format=format, cache=cache), expected)
