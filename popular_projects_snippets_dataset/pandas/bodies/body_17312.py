# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
obj = construct(frame_or_series, 5)
out = np.array([0])
errmsg = "the 'out' parameter is not supported"

with pytest.raises(ValueError, match=errmsg):
    obj.max(out=out)  # stat_function
with pytest.raises(ValueError, match=errmsg):
    obj.var(out=out)  # stat_function_ddof
with pytest.raises(ValueError, match=errmsg):
    obj.sum(out=out)  # cum_function
with pytest.raises(ValueError, match=errmsg):
    obj.any(out=out)  # logical_function
