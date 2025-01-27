# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 36031 implementing kahan summation
df = DataFrame(
    {"A": [3002399751580331.0 + add, -0.0, -0.0]},
    index=[
        Timestamp("19700101 09:00:00"),
        Timestamp("19700101 09:00:03"),
        Timestamp("19700101 09:00:06"),
    ],
)
result = (
    df.resample("1s").ffill().rolling("3s", closed="left", min_periods=3).mean()
)
dates = date_range("19700101 09:00:00", periods=7, freq="S")
expected = DataFrame(
    {
        "A": [
            np.nan,
            np.nan,
            np.nan,
            3002399751580330.5,
            2001599834386887.25,
            1000799917193443.625,
            0.0,
        ]
    },
    index=dates,
)
tm.assert_frame_equal(result, expected)
