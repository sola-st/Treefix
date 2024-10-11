# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# See discussion in GH#43487
gb = groupby_with_truncated_bingrouper

result = gb["Quantity"].aggregate(
    lambda values, index: np.nanmean(values), engine="numba"
)

expected = gb["Quantity"].aggregate(np.nanmean)
tm.assert_series_equal(result, expected)

result_df = gb[["Quantity"]].aggregate(
    lambda values, index: np.nanmean(values), engine="numba"
)
expected_df = gb[["Quantity"]].aggregate(np.nanmean)
tm.assert_frame_equal(result_df, expected_df)
