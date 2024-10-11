# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH#23925 _get_numeric_data may drop all columns
interpolation, method = interp_method
df = DataFrame(pd.date_range("1/1/18", periods=5))
df.columns.name = "captain tightpants"
result = df.quantile(
    0.5, numeric_only=True, interpolation=interpolation, method=method
)
expected = Series([], index=[], name=0.5, dtype=np.float64)
expected.index.name = "captain tightpants"
tm.assert_series_equal(result, expected)

result = df.quantile(
    [0.5], numeric_only=True, interpolation=interpolation, method=method
)
expected = DataFrame([], index=[0.5], columns=[])
expected.columns.name = "captain tightpants"
tm.assert_frame_equal(result, expected)
