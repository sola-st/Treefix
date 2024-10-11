# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
dr = date_range(start="2016-01-15", end="2016-01-20")

assert np.min(dr) == Timestamp("2016-01-15 00:00:00")
assert np.max(dr) == Timestamp("2016-01-20 00:00:00")

errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.min(dr, out=0)

with pytest.raises(ValueError, match=errmsg):
    np.max(dr, out=0)

assert np.argmin(dr) == 0
assert np.argmax(dr) == 5

errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.argmin(dr, out=0)

with pytest.raises(ValueError, match=errmsg):
    np.argmax(dr, out=0)
