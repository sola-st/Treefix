# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py

# GH 17496
# Resample nearest
index = date_range("1/1/2000", periods=3, freq="T")
result = Series(range(3), index=index).resample("20s").nearest()

expected = Series(
    [0, 0, 1, 1, 1, 2, 2],
    index=pd.DatetimeIndex(
        [
            "2000-01-01 00:00:00",
            "2000-01-01 00:00:20",
            "2000-01-01 00:00:40",
            "2000-01-01 00:01:00",
            "2000-01-01 00:01:20",
            "2000-01-01 00:01:40",
            "2000-01-01 00:02:00",
        ],
        dtype="datetime64[ns]",
        freq="20S",
    ),
)
tm.assert_series_equal(result, expected)
