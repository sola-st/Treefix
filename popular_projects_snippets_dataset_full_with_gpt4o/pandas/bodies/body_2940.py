# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# GH#44749
if using_array_manager and frame_or_series is DataFrame:
    mark = pytest.mark.xfail(reason=".values-based in-place check is invalid")
    request.node.add_marker(mark)

obj = frame_or_series([1, np.nan, 2])
orig = obj.values

obj.interpolate(inplace=True)
expected = frame_or_series([1, 1.5, 2])
tm.assert_equal(obj, expected)

# check we operated *actually* inplace
assert np.shares_memory(orig, obj.values)
assert orig.squeeze()[1] == 1.5
