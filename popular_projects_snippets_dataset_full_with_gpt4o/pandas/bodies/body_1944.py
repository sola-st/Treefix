# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py
# GH: 29485
df = DataFrame(
    {"value": pd.to_timedelta(np.arange(4), unit="s")},
    index=pd.date_range("20200101", periods=4, tz="UTC"),
)
result = df.resample("2D").quantile(0.99)
expected = DataFrame(
    {
        "value": [
            pd.Timedelta("0 days 00:00:00.990000"),
            pd.Timedelta("0 days 00:00:02.990000"),
        ]
    },
    index=pd.date_range("20200101", periods=2, tz="UTC", freq="2D"),
)
tm.assert_frame_equal(result, expected)
