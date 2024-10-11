# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# https://github.com/pandas-dev/pandas/issues/24752
df = DataFrame({"A": [1, 1], "B": [Timestamp("2000", tz=tz)] * 2})
result = df.mean()
expected = Series([1.0, Timestamp("2000", tz=tz)], index=["A", "B"])
tm.assert_series_equal(result, expected)
