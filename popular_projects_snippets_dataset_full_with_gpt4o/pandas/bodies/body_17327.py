# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
indices = [-3, 2, 0, 1]

obj = tm.makeTimeDataFrame()
obj = tm.get_obj(obj, frame_or_series)

msg = r"take\(\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg):
    obj.take(indices, foo=2)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    obj.take(indices, out=indices)

msg = "the 'mode' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    obj.take(indices, mode="clip")
