# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
df = DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=["a", "b", "c"])
result = df.quantile(
    [0.25, 0.5], axis=1, interpolation=interpolation, method=method
)
expected = DataFrame(
    [[1.0, 2.0, 3.0]] * 2, index=[0.25, 0.5], columns=[0, 1, 2]
)
if interpolation == "nearest":
    expected = expected.astype(np.int64)
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )
tm.assert_frame_equal(result, expected)
