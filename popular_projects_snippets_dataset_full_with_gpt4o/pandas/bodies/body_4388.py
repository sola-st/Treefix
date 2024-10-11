# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 14381
# Dict with None value
frame_none = DataFrame({"a": None}, index=[0])
frame_none_list = DataFrame({"a": [None]}, index=[0])
assert frame_none._get_value(0, "a") is None
assert frame_none_list._get_value(0, "a") is None
tm.assert_frame_equal(frame_none, frame_none_list)
