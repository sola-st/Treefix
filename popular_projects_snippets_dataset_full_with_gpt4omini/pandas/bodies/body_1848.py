# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

# since we are really doing an operation like this
# ts2.resample('2s').mean().ffill()
# preserve these semantics

rng = date_range("1/1/2012", periods=100, freq="S")
ts = Series(np.arange(len(rng)), index=rng)
ts2 = ts.iloc[[0, 1, 2, 3, 5, 7, 11, 15, 16, 25, 30]]

result = ts2.resample("2s").mean().ffill()
expected = Series(
    [
        0.5,
        2.5,
        5.0,
        7.0,
        7.0,
        11.0,
        11.0,
        15.0,
        16.0,
        16.0,
        16.0,
        16.0,
        25.0,
        25.0,
        25.0,
        30.0,
    ],
    index=pd.DatetimeIndex(
        [
            "2012-01-01 00:00:00",
            "2012-01-01 00:00:02",
            "2012-01-01 00:00:04",
            "2012-01-01 00:00:06",
            "2012-01-01 00:00:08",
            "2012-01-01 00:00:10",
            "2012-01-01 00:00:12",
            "2012-01-01 00:00:14",
            "2012-01-01 00:00:16",
            "2012-01-01 00:00:18",
            "2012-01-01 00:00:20",
            "2012-01-01 00:00:22",
            "2012-01-01 00:00:24",
            "2012-01-01 00:00:26",
            "2012-01-01 00:00:28",
            "2012-01-01 00:00:30",
        ],
        dtype="datetime64[ns]",
        freq="2S",
    ),
)
tm.assert_series_equal(result, expected)
