# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
# GH 20757
data = [["x", 1]]
columns = [("a", "b", np.nan), ("a", "c", 0.0)]
df = DataFrame(data, columns=MultiIndex.from_tuples(columns))
expected = df.dtypes.a.b
result = df.a.b.dtypes
tm.assert_series_equal(result, expected)
