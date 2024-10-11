# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# prod isn't defined on timedeltas
idx = ["a", "b", "c"]
df = DataFrame({"a": [0, 0], "b": [0, np.nan], "c": [np.nan, np.nan]})

df2 = df.apply(to_timedelta)

# 0 by default
result = df2.sum()
expected = Series([0, 0, 0], dtype="m8[ns]", index=idx)
tm.assert_series_equal(result, expected)

# min_count=0
result = df2.sum(min_count=0)
tm.assert_series_equal(result, expected)

# min_count=1
result = df2.sum(min_count=1)
expected = Series([0, 0, np.nan], dtype="m8[ns]", index=idx)
tm.assert_series_equal(result, expected)
