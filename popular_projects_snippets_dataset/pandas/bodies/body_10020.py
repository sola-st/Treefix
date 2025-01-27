# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_ewm.py
com = 3.0

# check variance debiasing factors
var_unbiased_x = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).var(bias=False)
var_biased_x = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).var(bias=True)

weights = create_mock_weights(all_data, com=com, adjust=adjust, ignore_na=ignore_na)
cum_sum = weights.cumsum().fillna(method="ffill")
cum_sum_sq = (weights * weights).cumsum().fillna(method="ffill")
numerator = cum_sum * cum_sum
denominator = numerator - cum_sum_sq
denominator[denominator <= 0.0] = np.nan
var_debiasing_factors_x = numerator / denominator

tm.assert_equal(var_unbiased_x, var_biased_x * var_debiasing_factors_x)
