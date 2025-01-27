# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_rolling.py
window, min_periods = rolling_consistency_cases

count_x = consistent_data.rolling(
    window=window, min_periods=min_periods, center=center
).count()
mean_x = consistent_data.rolling(
    window=window, min_periods=min_periods, center=center
).mean()
# check that correlation of a series with itself is either 1 or NaN
corr_x_x = consistent_data.rolling(
    window=window, min_periods=min_periods, center=center
).corr(consistent_data)

exp = (
    consistent_data.max()
    if isinstance(consistent_data, Series)
    else consistent_data.max().max()
)

# check mean of constant series
expected = consistent_data * np.nan
expected[count_x >= max(min_periods, 1)] = exp
tm.assert_equal(mean_x, expected)

# check correlation of constant series with itself is NaN
expected[:] = np.nan
tm.assert_equal(corr_x_x, expected)
