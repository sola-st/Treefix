# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
td = timedelta_range("16815 days", "16820 days", freq="D")

assert np.min(td) == Timedelta("16815 days")
assert np.max(td) == Timedelta("16820 days")

errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.min(td, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.max(td, out=0)

assert np.argmin(td) == 0
assert np.argmax(td) == 5

errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.argmin(td, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.argmax(td, out=0)
