# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
ts = frame_or_series(
    [0.0, 1.0, 2.0],
    index=DatetimeIndex(
        [
            datetime(2009, 10, 30),
            datetime(2009, 11, 30),
            datetime(2009, 12, 31),
        ],
        freq="BM",
    ),
)

daily_ts = ts.asfreq("B")
monthly_ts = daily_ts.asfreq("BM")
tm.assert_equal(monthly_ts, ts)

daily_ts = ts.asfreq("B", method="pad")
monthly_ts = daily_ts.asfreq("BM")
tm.assert_equal(monthly_ts, ts)

daily_ts = ts.asfreq(offsets.BDay())
monthly_ts = daily_ts.asfreq(offsets.BMonthEnd())
tm.assert_equal(monthly_ts, ts)

result = ts[:0].asfreq("M")
assert len(result) == 0
assert result is not ts

if frame_or_series is Series:
    daily_ts = ts.asfreq("D", fill_value=-1)
    result = daily_ts.value_counts().sort_index()
    expected = Series([60, 1, 1, 1], index=[-1.0, 2.0, 1.0, 0.0]).sort_index()
    tm.assert_series_equal(result, expected)
