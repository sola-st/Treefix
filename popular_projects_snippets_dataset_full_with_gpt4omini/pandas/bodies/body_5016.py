# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
s = pd.Series([1, NA], dtype=object)
expected = pd.Series([False, True])
tm.assert_series_equal(s.isna(), expected)
