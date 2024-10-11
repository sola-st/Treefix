# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
if method == "table" and using_array_manager:
    request.node.add_marker(
        pytest.mark.xfail(reason="Axis name incorrectly set.")
    )
# GH 14357 - float block where some cols have missing values
df = DataFrame({"a": np.arange(1, 6.0), "b": np.arange(1, 6.0)})
df.iloc[-1, 1] = np.nan

res = df.quantile(0.5, interpolation=interpolation, method=method)
exp = Series(
    [3.0, 2.5 if interpolation == "linear" else 3.0], index=["a", "b"], name=0.5
)
tm.assert_series_equal(res, exp)

res = df.quantile([0.5, 0.75], interpolation=interpolation, method=method)
exp = DataFrame(
    {
        "a": [3.0, 4.0],
        "b": [2.5, 3.25] if interpolation == "linear" else [3.0, 4.0],
    },
    index=[0.5, 0.75],
)
tm.assert_frame_equal(res, exp)

res = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)
exp = Series(np.arange(1.0, 6.0), name=0.5)
tm.assert_series_equal(res, exp)

res = df.quantile(
    [0.5, 0.75], axis=1, interpolation=interpolation, method=method
)
exp = DataFrame([np.arange(1.0, 6.0)] * 2, index=[0.5, 0.75])
if interpolation == "nearest":
    exp.iloc[1, -1] = np.nan
tm.assert_frame_equal(res, exp)

# full-nan column
df["b"] = np.nan

res = df.quantile(0.5, interpolation=interpolation, method=method)
exp = Series([3.0, np.nan], index=["a", "b"], name=0.5)
tm.assert_series_equal(res, exp)

res = df.quantile([0.5, 0.75], interpolation=interpolation, method=method)
exp = DataFrame({"a": [3.0, 4.0], "b": [np.nan, np.nan]}, index=[0.5, 0.75])
tm.assert_frame_equal(res, exp)
