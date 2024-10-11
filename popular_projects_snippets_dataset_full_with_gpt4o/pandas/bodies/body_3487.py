# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )
# full NaT column
df = DataFrame({"a": [pd.NaT, pd.NaT, pd.NaT]})

res = df.quantile(
    0.5, numeric_only=False, interpolation=interpolation, method=method
)
exp = Series([pd.NaT], index=["a"], name=0.5)
tm.assert_series_equal(res, exp)

res = df.quantile(
    [0.5], numeric_only=False, interpolation=interpolation, method=method
)
exp = DataFrame({"a": [pd.NaT]}, index=[0.5])
tm.assert_frame_equal(res, exp)

# mixed non-null / full null column
df = DataFrame(
    {
        "a": [
            Timestamp("2012-01-01"),
            Timestamp("2012-01-02"),
            Timestamp("2012-01-03"),
        ],
        "b": [pd.NaT, pd.NaT, pd.NaT],
    }
)

res = df.quantile(
    0.5, numeric_only=False, interpolation=interpolation, method=method
)
exp = Series([Timestamp("2012-01-02"), pd.NaT], index=["a", "b"], name=0.5)
tm.assert_series_equal(res, exp)

res = df.quantile(
    [0.5], numeric_only=False, interpolation=interpolation, method=method
)
exp = DataFrame(
    [[Timestamp("2012-01-02"), pd.NaT]], index=[0.5], columns=["a", "b"]
)
tm.assert_frame_equal(res, exp)
