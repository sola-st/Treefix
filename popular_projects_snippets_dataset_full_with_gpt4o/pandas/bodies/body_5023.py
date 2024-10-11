# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
# https://github.com/pandas-dev/pandas/issues/31847
result = pickle.loads(pickle.dumps(NA))
assert result is NA
