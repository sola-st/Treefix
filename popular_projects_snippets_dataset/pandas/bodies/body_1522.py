# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH24924
s = Series([1, 2])
result = s.loc[np.array(0)]
assert result == 1
