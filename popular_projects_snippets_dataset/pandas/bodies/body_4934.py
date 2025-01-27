# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
pr = pd.period_range(start="2016-01-15", end="2016-01-20")

assert np.min(pr) == Period("2016-01-15", freq="D")
assert np.max(pr) == Period("2016-01-20", freq="D")

errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.min(pr, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.max(pr, out=0)

assert np.argmin(pr) == 0
assert np.argmax(pr) == 5

errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.argmin(pr, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.argmax(pr, out=0)
