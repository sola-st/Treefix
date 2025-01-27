# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py

ser = Series(
    [
        Timestamp("20130101"),
        Timestamp("20130101"),
        Timestamp("20130102"),
        Timestamp("20130103 9:01:01"),
    ]
)
ser[2] = np.nan

# ffill
result = ser.ffill()
expected = Series(
    [
        Timestamp("20130101"),
        Timestamp("20130101"),
        Timestamp("20130101"),
        Timestamp("20130103 9:01:01"),
    ]
)
tm.assert_series_equal(result, expected)

# bfill
result = ser.bfill()
expected = Series(
    [
        Timestamp("20130101"),
        Timestamp("20130101"),
        Timestamp("20130103 9:01:01"),
        Timestamp("20130103 9:01:01"),
    ]
)
tm.assert_series_equal(result, expected)
