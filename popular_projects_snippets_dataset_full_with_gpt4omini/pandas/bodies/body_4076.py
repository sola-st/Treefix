# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# https://github.com/pandas-dev/pandas/issues/39738
df = DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
result = df.sum(min_count=10)
expected = Series([np.nan, np.nan], index=["x", "y"])
tm.assert_series_equal(result, expected)
