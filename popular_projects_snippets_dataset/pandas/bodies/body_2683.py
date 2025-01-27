# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename_axis.py
# GH#15704
expected = float_frame.rename_axis("foo")
result = float_frame.copy()
return_value = no_return = result.rename_axis("foo", inplace=True)
assert return_value is None

assert no_return is None
tm.assert_frame_equal(result, expected)

expected = float_frame.rename_axis("bar", axis=1)
result = float_frame.copy()
return_value = no_return = result.rename_axis("bar", axis=1, inplace=True)
assert return_value is None

assert no_return is None
tm.assert_frame_equal(result, expected)
