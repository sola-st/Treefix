# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH24924
df = DataFrame([[1, 2], [3, 4]])
result = df.loc[np.array(0)]
s = Series([1, 2], name=0)
tm.assert_series_equal(result, s)
