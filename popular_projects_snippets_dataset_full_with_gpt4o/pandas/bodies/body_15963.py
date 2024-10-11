# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_value_counts.py
values = [
    pd.Period("2011-01", freq="M"),
    pd.Period("2011-02", freq="M"),
    pd.Period("2011-03", freq="M"),
    pd.Period("2011-01", freq="M"),
    pd.Period("2011-01", freq="M"),
    pd.Period("2011-03", freq="M"),
]

exp_idx = pd.PeriodIndex(["2011-01", "2011-03", "2011-02"], freq="M")
exp = Series([3, 2, 1], index=exp_idx, name="xxx")

ser = Series(values, name="xxx")
tm.assert_series_equal(ser.value_counts(), exp)
# check DatetimeIndex outputs the same result
idx = pd.PeriodIndex(values, name="xxx")
tm.assert_series_equal(idx.value_counts(), exp)

# normalize
exp = Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name="xxx")
tm.assert_series_equal(ser.value_counts(normalize=True), exp)
tm.assert_series_equal(idx.value_counts(normalize=True), exp)
