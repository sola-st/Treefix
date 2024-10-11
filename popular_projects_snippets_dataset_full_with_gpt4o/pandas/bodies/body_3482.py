# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH#41544
interpolation, method = interp_method
df = DataFrame(columns=["a", "b"], dtype=dtype)

res = df.quantile(
    0.5, axis=1, numeric_only=False, interpolation=interpolation, method=method
)
expected = Series([], index=[], name=0.5, dtype=dtype)
tm.assert_series_equal(res, expected)

# no columns in result, so no dtype preservation
res = df.quantile(
    [0.5],
    axis=1,
    numeric_only=False,
    interpolation=interpolation,
    method=method,
)
expected = DataFrame(index=[0.5], columns=[])
tm.assert_frame_equal(res, expected)
