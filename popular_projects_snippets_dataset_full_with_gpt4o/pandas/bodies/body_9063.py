# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
# GH#32501 warn when losing timezone information
dti = pd.date_range("2016-01-01", periods=3, tz="US/Pacific")

expected = SparseArray(np.asarray(dti, dtype="datetime64[ns]"))

with tm.assert_produces_warning(UserWarning):
    result = SparseArray(dti)

tm.assert_sp_array_equal(result, expected)

with tm.assert_produces_warning(UserWarning):
    result = SparseArray(pd.Series(dti))

tm.assert_sp_array_equal(result, expected)
