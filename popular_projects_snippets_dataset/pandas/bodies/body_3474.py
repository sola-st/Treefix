# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH 9543/9544
interpolation, method = interp_method
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )
df = DataFrame({"A": [1, 2, 3], "B": [2, 3, 4]}, index=[1, 2, 3])

result = df.quantile(0.5, axis=0, interpolation=interpolation, method=method)

expected = Series([2.0, 3.0], index=["A", "B"], name=0.5)
if interpolation == "nearest":
    expected = expected.astype(np.int64)
tm.assert_series_equal(result, expected)

expected = df.quantile(
    0.5, axis="index", interpolation=interpolation, method=method
)
if interpolation == "nearest":
    expected = expected.astype(np.int64)
tm.assert_series_equal(result, expected)

result = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)

expected = Series([1.5, 2.5, 3.5], index=[1, 2, 3], name=0.5)
if interpolation == "nearest":
    expected = expected.astype(np.int64)
tm.assert_series_equal(result, expected)

result = df.quantile(
    0.5, axis="columns", interpolation=interpolation, method=method
)
tm.assert_series_equal(result, expected)

msg = "No axis named -1 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.quantile(0.1, axis=-1, interpolation=interpolation, method=method)
msg = "No axis named column for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.quantile(0.1, axis="column")
