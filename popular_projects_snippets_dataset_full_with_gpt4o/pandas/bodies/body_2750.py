# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_truncate.py
# GH#17935

obj = DataFrame({"A": ["a", "b", "c", "d", "e"]}, index=[5, 3, 2, 9, 0])
obj = tm.get_obj(obj, frame_or_series)

msg = "truncate requires a sorted index"
with pytest.raises(ValueError, match=msg):
    obj.truncate(before=3, after=9)
