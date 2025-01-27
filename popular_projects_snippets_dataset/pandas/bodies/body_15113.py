# Extracted from ./data/repos/pandas/pandas/tests/base/test_value_counts.py
# GH31944
klass = index_or_series
values = [True, pd.NA, np.nan]
obj = klass(values)
res = obj.value_counts(dropna=dropna)
if dropna is True:
    expected = Series([1], index=Index([True], dtype=obj.dtype))
else:
    expected = Series([1, 1, 1], index=[True, pd.NA, np.nan])
tm.assert_series_equal(res, expected)
