# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# GH 12918
if using_array_manager and axis in (1, "columns"):
    # TODO(ArrayManager) support axis=1
    td.mark_array_manager_not_yet_implemented(request)

df = DataFrame(
    {
        "A": [1.0, 2.0, 3.0, 4.0, np.nan, 5.0],
        "B": [2.0, 4.0, 6.0, np.nan, 8.0, 10.0],
        "C": [3.0, 6.0, 9.0, np.nan, np.nan, 30.0],
    }
)
expected = df.fillna(axis=axis, method=method)
result = df.interpolate(method=method, axis=axis)
tm.assert_frame_equal(result, expected)
