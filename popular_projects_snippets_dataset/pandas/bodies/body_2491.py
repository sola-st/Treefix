# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# https://github.com/pandas-dev/pandas/issues/23559
data = SparseArray([0, 1])
df = DataFrame({"A": data})
expected = Series(data, name="A")
result = df["A"]
tm.assert_series_equal(result, expected)

# Also check iloc and loc while we're here
result = df.iloc[:, 0]
tm.assert_series_equal(result, expected)

result = df.loc[:, "A"]
tm.assert_series_equal(result, expected)
