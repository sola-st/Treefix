# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH #995
s = float_frame["C"].copy()
s.name = None

result = s.groupby(float_frame["A"]).agg(np.sum)
assert result.name is None
