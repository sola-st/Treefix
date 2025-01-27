# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_ewm.py
com = 3.0

result = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).mean()
weights = create_mock_weights(all_data, com=com, adjust=adjust, ignore_na=ignore_na)
expected = (
    all_data.multiply(weights)
    .cumsum()
    .divide(weights.cumsum())
    .fillna(method="ffill")
)
expected[
    all_data.expanding().count() < (max(min_periods, 1) if min_periods else 1)
] = np.nan
tm.assert_equal(result, expected.astype("float64"))
