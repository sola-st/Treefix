# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
assert isna(np.array(np.nan))
assert not isna(np.array(0.0))
assert not isna(np.array(0))
# test object dtype
assert isna(np.array(np.nan, dtype=object))
assert not isna(np.array(0.0, dtype=object))
assert not isna(np.array(0, dtype=object))
