# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# https://github.com/pandas-dev/pandas/issues/24752
# Behavior in 0.24.0rc1 was buggy.
# As of 2.0 with numeric_only=None we do *not* drop datetime columns
df = DataFrame({"A": [Timestamp("2000", tz=tz)] * 2})
result = df.mean()

expected = Series([Timestamp("2000", tz=tz)], index=["A"])
tm.assert_series_equal(result, expected)
