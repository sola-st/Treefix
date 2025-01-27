# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
assert np.log(NA) is NA
assert np.add(NA, 1) is NA
result = np.divmod(NA, 1)
assert result[0] is NA and result[1] is NA

result = np.frexp(NA)
assert result[0] is NA and result[1] is NA
