# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_dropna.py
# DatetimeLikeBlock
ser = Series(
    [
        Timestamp("2011-01-01 10:00"),
        NaT,
        Timestamp("2011-01-03 10:00"),
        NaT,
    ]
)
result = ser.dropna()
expected = Series(
    [Timestamp("2011-01-01 10:00"), Timestamp("2011-01-03 10:00")], index=[0, 2]
)
tm.assert_series_equal(result, expected)

# DatetimeTZBlock
idx = DatetimeIndex(
    ["2011-01-01 10:00", NaT, "2011-01-03 10:00", NaT], tz="Asia/Tokyo"
)
ser = Series(idx)
assert ser.dtype == "datetime64[ns, Asia/Tokyo]"
result = ser.dropna()
expected = Series(
    [
        Timestamp("2011-01-01 10:00", tz="Asia/Tokyo"),
        Timestamp("2011-01-03 10:00", tz="Asia/Tokyo"),
    ],
    index=[0, 2],
)
assert result.dtype == "datetime64[ns, Asia/Tokyo]"
tm.assert_series_equal(result, expected)
