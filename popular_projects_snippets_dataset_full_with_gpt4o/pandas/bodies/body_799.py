# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py

assert not libmissing.is_matching_na(None, np.nan)
assert not libmissing.is_matching_na(np.nan, None)

assert libmissing.is_matching_na(None, np.nan, nan_matches_none=True)
assert libmissing.is_matching_na(np.nan, None, nan_matches_none=True)
