# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
if op_name == "count":
    result = getattr(s, op_name)()
    expected = getattr(s.astype("float64"), op_name)()
else:
    result = getattr(s, op_name)(skipna=skipna)
    expected = getattr(s.astype("float64"), op_name)(skipna=skipna)
# override parent function to cast to bool for min/max
if np.isnan(expected):
    expected = pd.NA
elif op_name in ("min", "max"):
    expected = bool(expected)
tm.assert_almost_equal(result, expected)
