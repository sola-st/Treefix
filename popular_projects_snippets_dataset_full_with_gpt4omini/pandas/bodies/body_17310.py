# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
obj = construct(frame_or_series, 5)
starwars = "Star Wars"
errmsg = "unexpected keyword"

with pytest.raises(TypeError, match=errmsg):
    obj.max(epic=starwars)  # stat_function
with pytest.raises(TypeError, match=errmsg):
    obj.var(epic=starwars)  # stat_function_ddof
with pytest.raises(TypeError, match=errmsg):
    obj.sum(epic=starwars)  # cum_function
with pytest.raises(TypeError, match=errmsg):
    obj.any(epic=starwars)  # logical_function
