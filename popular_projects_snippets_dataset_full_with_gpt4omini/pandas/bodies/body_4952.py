# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# Check skipna, with implicit 'object' dtype.
s1 = Series([np.nan, True])
s2 = Series([np.nan, False])
assert s1.all(skipna=False)  # nan && True => True
assert s1.all(skipna=True)
assert s2.any(skipna=False)
assert not s2.any(skipna=True)
