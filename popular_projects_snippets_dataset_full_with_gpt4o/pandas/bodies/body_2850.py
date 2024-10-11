# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# with timezone in another column
# GH#15522
df = DataFrame(
    {
        "A": date_range("20130101", periods=4, tz="US/Eastern"),
        "B": [1, 2, np.nan, np.nan],
    }
)
result = df.fillna(method="pad")
expected = DataFrame(
    {
        "A": date_range("20130101", periods=4, tz="US/Eastern"),
        "B": [1.0, 2.0, 2.0, 2.0],
    }
)
tm.assert_frame_equal(result, expected)
