# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_clip.py
# GH#15388
median = float_frame.median().median()
frame_copy = float_frame.copy()

return_value = frame_copy.clip(upper=median, lower=median, inplace=True)
assert return_value is None
assert not (frame_copy.values != median).any()
