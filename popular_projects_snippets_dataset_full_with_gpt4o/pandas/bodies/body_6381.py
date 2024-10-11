# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
result = getattr(s, op_name)(skipna=skipna)
expected = getattr(pd.Series(s.astype("float64")), op_name)(skipna=skipna)
tm.assert_series_equal(result, expected, check_dtype=False)
if op_name in ("cummin", "cummax"):
    assert is_bool_dtype(result)
