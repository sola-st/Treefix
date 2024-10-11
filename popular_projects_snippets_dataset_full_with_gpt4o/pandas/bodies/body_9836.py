# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH-28192
tz = tz_naive_fixture
df = DataFrame(
    {i: [1] * 2 for i in date_range("2019-8-01", "2019-08-03", freq="D", tz=tz)}
)
if axis_frame in [0, "index"]:
    result = df.T.rolling("2D", axis=axis_frame).sum().T
else:
    result = df.rolling("2D", axis=axis_frame).sum()
expected = DataFrame(
    {
        **{
            i: [1.0] * 2
            for i in date_range("2019-8-01", periods=1, freq="D", tz=tz)
        },
        **{
            i: [2.0] * 2
            for i in date_range("2019-8-02", "2019-8-03", freq="D", tz=tz)
        },
    }
)
tm.assert_frame_equal(result, expected)
