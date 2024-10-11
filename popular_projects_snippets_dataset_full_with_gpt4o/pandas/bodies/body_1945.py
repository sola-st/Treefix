# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py
# GH#45414
idx = pd.Index([pd.Timedelta(seconds=120 + i * 30) for i in range(10)])
ser = Series(range(10), index=idx)
result = ser.resample("T", closed="right", label="right").sum()
expected = Series(
    [0, 3, 7, 11, 15, 9],
    index=pd.TimedeltaIndex(
        [pd.Timedelta(seconds=120 + i * 60) for i in range(6)], freq="T"
    ),
)
tm.assert_series_equal(result, expected)
