# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
arr = pd.array([1, 2, pd.NA, 4], dtype=any_numeric_ea_dtype)
ser = pd.Series(arr)

self._check_replace_with_method(ser)
