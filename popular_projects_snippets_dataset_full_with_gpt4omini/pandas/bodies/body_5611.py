# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH#48019
ser = Series([1, pd.NA, 2] * 3, dtype=any_numeric_ea_dtype)
result = pd.unique(ser)
expected = pd.array([1, pd.NA, 2], dtype=any_numeric_ea_dtype)
tm.assert_extension_array_equal(result, expected)
