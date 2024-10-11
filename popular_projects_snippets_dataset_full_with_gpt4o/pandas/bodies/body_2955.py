# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# TODO(CoW) inplace keyword (it is still mutating the parent)
if using_copy_on_write:
    pytest.skip("CoW: inplace keyword not yet handled")
df = DataFrame({"a": [1.0, 2.0, np.nan, 4.0]})
expected = DataFrame({"a": [1.0, 2.0, 3.0, 4.0]})
result = df.copy()
return_value = result["a"].interpolate(inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)

result = df.copy()
return_value = result["a"].interpolate(inplace=True, downcast="infer")
assert return_value is None
tm.assert_frame_equal(result, expected.astype("int64"))
