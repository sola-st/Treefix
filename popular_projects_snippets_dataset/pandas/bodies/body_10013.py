# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_rolling.py
window, min_periods = rolling_consistency_cases

result = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).mean()
expected = (
    all_data.rolling(window=window, min_periods=min_periods, center=center)
    .sum()
    .divide(
        all_data.rolling(
            window=window, min_periods=min_periods, center=center
        ).count()
    )
)
tm.assert_equal(result, expected.astype("float64"))
