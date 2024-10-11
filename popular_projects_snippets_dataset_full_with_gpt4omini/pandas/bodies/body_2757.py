# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_and_last.py
# GH#20725
obj = DataFrame([[1, 2, 3], [4, 5, 6]])
obj = tm.get_obj(obj, frame_or_series)

msg = "'first' only supports a DatetimeIndex index"
with pytest.raises(TypeError, match=msg):  # index is not a DatetimeIndex
    obj.first("1D")

msg = "'last' only supports a DatetimeIndex index"
with pytest.raises(TypeError, match=msg):  # index is not a DatetimeIndex
    obj.last("1D")
