# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH 2460
interpolation, method = interp_method
dti = pd.date_range("2016-01-01", periods=3, tz="US/Pacific")
ser = Series(dti)
df = DataFrame(ser)

result = df.quantile(
    numeric_only=False, interpolation=interpolation, method=method
)
expected = Series(
    ["2016-01-02 00:00:00"], name=0.5, dtype="datetime64[ns, US/Pacific]"
)
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )

tm.assert_series_equal(result, expected)
