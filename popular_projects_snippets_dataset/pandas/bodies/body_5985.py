# Extracted from ./data/repos/pandas/pandas/tests/extension/test_integer.py
# overwrite to ensure pd.NA is tested instead of np.nan
# https://github.com/pandas-dev/pandas/issues/30958
if op_name == "count":
    result = getattr(s, op_name)()
    expected = getattr(s.dropna().astype("int64"), op_name)()
else:
    result = getattr(s, op_name)(skipna=skipna)
    expected = getattr(s.dropna().astype("int64"), op_name)(skipna=skipna)
    if not skipna and s.isna().any():
        expected = pd.NA
tm.assert_almost_equal(result, expected)
