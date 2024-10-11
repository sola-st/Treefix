# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH 6766
df1 = DataFrame([{"A": None, "B": 1}, {"A": 2, "B": 2}])
df2 = DataFrame([{"A": 3, "B": 3}, {"A": 4, "B": 4}])
df = concat([df1, df2], axis=1)

# cross-sectional indexing
result = df.iloc[0, 0]
assert isna(result)

result = df.iloc[0, :]
expected = Series([np.nan, 1, 3, 3], index=["A", "B", "A", "B"], name=0)
tm.assert_series_equal(result, expected)
