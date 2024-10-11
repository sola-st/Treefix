# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
result = DataFrame({"x": [], "y": []}).quantile(
    [0.1, 0.9], axis=0, interpolation=interpolation, method=method
)
expected = DataFrame(
    {"x": [np.nan, np.nan], "y": [np.nan, np.nan]}, index=[0.1, 0.9]
)
tm.assert_frame_equal(result, expected)
