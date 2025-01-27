# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
dtype = CategoricalDtype(categories=[0, 1, 2])
assert is_valid_na_for_dtype(np.nan, dtype)

assert not is_valid_na_for_dtype(NaT, dtype)
assert not is_valid_na_for_dtype(np.datetime64("NaT", "ns"), dtype)
assert not is_valid_na_for_dtype(np.timedelta64("NaT", "ns"), dtype)
