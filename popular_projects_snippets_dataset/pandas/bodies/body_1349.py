# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH24919
df = DataFrame([[1, 2], [3, 4]])
result = df.iloc[np.array(0)]
s = Series([1, 2], name=0)
tm.assert_series_equal(result, s)
