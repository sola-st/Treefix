# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# We may want to break API in the future to change this
# so that we exclude non-numeric along the same axis
# See GH #7312
interpolation, method = interp_method
df = DataFrame([[1, 2, 3], ["a", "b", 4]])
result = df.quantile(
    0.5, axis=1, numeric_only=True, interpolation=interpolation, method=method
)
expected = Series([3.0, 4.0], index=[0, 1], name=0.5)
if interpolation == "nearest":
    expected = expected.astype(np.int64)
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )
tm.assert_series_equal(result, expected)
