# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH42688, nans aren't mangled
nulls = [pd.NA, np.nan, pd.NaT, None]
values = np.array([True] + nulls * 2, dtype=np.object_)
modes = ht.mode(values, False)
assert modes.size == len(nulls)
