# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# axis
interpolation, method = interp_method
df = DataFrame({"A": [1, 2, 3], "B": [2, 3, 4]}, index=[1, 2, 3])
result = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)
expected = Series([1.5, 2.5, 3.5], index=[1, 2, 3], name=0.5)
if interpolation == "nearest":
    expected = expected.astype(np.int64)
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )
tm.assert_series_equal(result, expected)

result = df.quantile(
    [0.5, 0.75], axis=1, interpolation=interpolation, method=method
)
expected = DataFrame(
    {1: [1.5, 1.75], 2: [2.5, 2.75], 3: [3.5, 3.75]}, index=[0.5, 0.75]
)
if interpolation == "nearest":
    expected.iloc[0, :] -= 0.5
    expected.iloc[1, :] += 0.25
    expected = expected.astype(np.int64)
tm.assert_frame_equal(result, expected, check_index_type=True)
