# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# GH 10395
result = DataFrame(
    {"a": [1.0, 2.0, 3.0, 4.0], "b": [np.nan, 2.0, 3.0, 4.0], "c": [3, 2, 2, 2]}
)
expected = result.interpolate(method="linear", axis=1, inplace=False)
return_value = result.interpolate(method="linear", axis=1, inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)
