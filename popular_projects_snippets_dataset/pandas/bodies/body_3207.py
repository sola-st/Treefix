# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
# GH#9854
index_name = "bar"
index = date_range("20130101", periods=20, name=index_name)
obj = DataFrame(list(range(20)), columns=["foo"], index=index)
obj = tm.get_obj(obj, frame_or_series)

assert index_name == obj.index.name
assert index_name == obj.asfreq("10D").index.name
