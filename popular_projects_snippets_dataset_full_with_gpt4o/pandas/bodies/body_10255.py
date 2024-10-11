# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH#43500 Previously raised ValueError bc used index with incorrect
#  length in wrap_applied_result
gb = groupby_with_truncated_bingrouper

res = gb["Quantity"].apply(lambda x: x.iloc[0] if len(x) else np.nan)

dti = date_range("2013-09-01", "2013-10-01", freq="5D", name="Date")
expected = Series(
    [18, np.nan, np.nan, np.nan, np.nan, np.nan, 5],
    index=dti._with_freq(None),
    name="Quantity",
)

tm.assert_series_equal(res, expected)
