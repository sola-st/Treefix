# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# gh 21662
df = pd.DataFrame([0, 1, np.nan, 3], index=ind)

method, kwargs = interp_methods_ind
if method == "pchip":
    pytest.importorskip("scipy")

if method == "linear":
    result = df[0].interpolate(**kwargs)
    expected = Series([0.0, 1.0, 2.0, 3.0], name=0, index=ind)
    tm.assert_series_equal(result, expected)
else:
    expected_error = (
        "Index column must be numeric or datetime type when "
        f"using {method} method other than linear. "
        "Try setting a numeric or datetime index column before "
        "interpolating."
    )
    with pytest.raises(ValueError, match=expected_error):
        df[0].interpolate(method=method, **kwargs)
