# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#17667
df = DataFrame(
    {
        "a": Series([0, 0]),
        "t": Series([to_timedelta(0, "s"), to_timedelta(1, "ms")]),
    }
)

result = df.any(axis=0)
expected = Series(data=[False, True], index=["a", "t"])
tm.assert_series_equal(result, expected)

result = df.any(axis=1)
expected = Series(data=[False, True])
tm.assert_series_equal(result, expected)
