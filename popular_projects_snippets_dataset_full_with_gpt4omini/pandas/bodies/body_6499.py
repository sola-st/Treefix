# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py

if op_name in ["median", "skew", "kurt", "sem"]:
    msg = r"decimal does not support the .* operation"
    with pytest.raises(NotImplementedError, match=msg):
        getattr(s, op_name)(skipna=skipna)
elif op_name == "count":
    result = getattr(s, op_name)()
    expected = len(s) - s.isna().sum()
    tm.assert_almost_equal(result, expected)
else:
    result = getattr(s, op_name)(skipna=skipna)
    expected = getattr(np.asarray(s), op_name)()
    tm.assert_almost_equal(result, expected)
