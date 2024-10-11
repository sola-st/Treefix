# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
# GH#20725
obj = DataFrame([[1, 2, 3], [4, 5, 6]])
obj = tm.get_obj(obj, frame_or_series)

msg = "Index must be DatetimeIndex"
with pytest.raises(TypeError, match=msg):  # index is not a DatetimeIndex
    obj.between_time(start_time="00:00", end_time="12:00")
