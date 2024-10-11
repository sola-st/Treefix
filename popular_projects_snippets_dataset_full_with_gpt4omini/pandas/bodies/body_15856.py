# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 38267
result = pd.Series([0, None], dtype=any_int_ea_dtype).replace(0, pd.NA)
expected = pd.Series([pd.NA, pd.NA], dtype=any_int_ea_dtype)
tm.assert_series_equal(result, expected)
result = pd.Series([0, 1], dtype=any_int_ea_dtype).replace(0, pd.NA)
result.replace(1, pd.NA, inplace=True)
tm.assert_series_equal(result, expected)
