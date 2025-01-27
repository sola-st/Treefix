# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#26125
idx = RangeIndex(0, 10, 3)

result = np.max(idx)
assert result == 9

result = np.min(idx)
assert result == 0

errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.min(idx, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.max(idx, out=0)
