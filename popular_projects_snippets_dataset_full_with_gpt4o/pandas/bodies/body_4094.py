# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# don't cast to object, which would raise in nanops
dti = date_range("2016-01-01", periods=3)

# Copying dti is needed for ArrayManager otherwise when we set
#  df.loc[0, 3] = pd.NaT below it edits dti
df = DataFrame({1: [0, 2, 1], 2: range(3)[::-1], 3: dti.copy(deep=True)})

result = df.idxmax()
expected = Series([1, 0, 2], index=[1, 2, 3])
tm.assert_series_equal(result, expected)

result = df.idxmin()
expected = Series([0, 2, 0], index=[1, 2, 3])
tm.assert_series_equal(result, expected)

# with NaTs
df.loc[0, 3] = pd.NaT
result = df.idxmax()
expected = Series([1, 0, 2], index=[1, 2, 3])
tm.assert_series_equal(result, expected)

result = df.idxmin()
expected = Series([0, 2, 1], index=[1, 2, 3])
tm.assert_series_equal(result, expected)

# with multi-column dt64 block
df[4] = dti[::-1]
df._consolidate_inplace()

result = df.idxmax()
expected = Series([1, 0, 2, 0], index=[1, 2, 3, 4])
tm.assert_series_equal(result, expected)

result = df.idxmin()
expected = Series([0, 2, 1, 2], index=[1, 2, 3, 4])
tm.assert_series_equal(result, expected)
