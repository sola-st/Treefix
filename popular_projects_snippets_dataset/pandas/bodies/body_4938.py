# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

# GH#34814
# consistency for nullable dtypes on empty or ALL-NA mean

# empty series
eser = Series([], dtype=dtype)
result = getattr(eser, method)()
assert result is pd.NA

# ALL-NA series
nser = Series([np.nan], dtype=dtype)
result = getattr(nser, method)()
assert result is pd.NA
