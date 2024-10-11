# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
dti = date_range("2016-01-01", periods=3)
df = DataFrame({3: dti, 4: dti[::-1]}, copy=True)
df.iloc[0, 0] = pd.NaT

df._consolidate_inplace()

result = df.idxmax(axis=1)
expected = Series([4, 3, 3])
tm.assert_series_equal(result, expected)

result = df.idxmin(axis=1)
expected = Series([4, 3, 4])
tm.assert_series_equal(result, expected)
