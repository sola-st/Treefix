# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# https://github.com/pandas-dev/pandas/issues/25014
dtz = pd.DatetimeTZDtype(tz="UTC")
right = DataFrame(
    {
        "date": [pd.Timestamp("2018", tz=dtz.tz)],
        "value": [4.0],
        "date2": [pd.Timestamp("2019", tz=dtz.tz)],
    },
    columns=["date", "value", "date2"],
)
left = right[:0]
result = left.merge(right, on="date")
expected = DataFrame(
    {
        "value_x": Series(dtype=float),
        "date2_x": Series(dtype=dtz),
        "date": Series(dtype=dtz),
        "value_y": Series(dtype=float),
        "date2_y": Series(dtype=dtz),
    },
    columns=["value_x", "date2_x", "date", "value_y", "date2_y"],
)
tm.assert_frame_equal(result, expected)
