# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py

# mixed on axis=1
interpolation, method = interp_method
df = DataFrame(
    {
        "A": [1, 2, 3],
        "B": [2.0, 3.0, 4.0],
        "C": pd.date_range("20130101", periods=3),
        "D": ["foo", "bar", "baz"],
    }
)
result = df.quantile(
    0.5, axis=1, numeric_only=True, interpolation=interpolation, method=method
)
expected = Series([1.5, 2.5, 3.5], name=0.5)
if interpolation == "nearest":
    expected -= 0.5
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )
tm.assert_series_equal(result, expected)

# must raise
msg = "'<' not supported between instances of 'Timestamp' and 'float'"
with pytest.raises(TypeError, match=msg):
    df.quantile(0.5, axis=1, numeric_only=False)
