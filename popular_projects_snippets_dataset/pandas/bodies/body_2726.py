# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_clip.py
# GH#15390
original = simple_frame.copy(deep=True)

result = original.clip(lower=lower, upper=[5, 6, 7], axis=axis, inplace=inplace)

expected = DataFrame(res, columns=original.columns, index=original.index)
if inplace:
    result = original
tm.assert_frame_equal(result, expected, check_exact=True)
