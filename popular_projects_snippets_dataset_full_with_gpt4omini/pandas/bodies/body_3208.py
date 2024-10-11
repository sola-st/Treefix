# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
index = period_range(freq="A", start="1/1/2001", end="12/31/2010")
obj = DataFrame(np.random.randn(len(index), 3), index=index)
obj = tm.get_obj(obj, frame_or_series)

result = obj.asfreq("D", how="end")
exp_index = index.asfreq("D", how="end")
assert len(result) == len(obj)
tm.assert_index_equal(result.index, exp_index)

result = obj.asfreq("D", how="start")
exp_index = index.asfreq("D", how="start")
assert len(result) == len(obj)
tm.assert_index_equal(result.index, exp_index)
