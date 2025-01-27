# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_value_counts.py
# most dtypes are tested in tests/base
values = [
    pd.Timestamp("2011-01-01 09:00"),
    pd.Timestamp("2011-01-01 10:00"),
    pd.Timestamp("2011-01-01 11:00"),
    pd.Timestamp("2011-01-01 09:00"),
    pd.Timestamp("2011-01-01 09:00"),
    pd.Timestamp("2011-01-01 11:00"),
]

exp_idx = pd.DatetimeIndex(
    ["2011-01-01 09:00", "2011-01-01 11:00", "2011-01-01 10:00"]
)
exp = Series([3, 2, 1], index=exp_idx, name="xxx")

ser = Series(values, name="xxx")
tm.assert_series_equal(ser.value_counts(), exp)
# check DatetimeIndex outputs the same result
idx = pd.DatetimeIndex(values, name="xxx")
tm.assert_series_equal(idx.value_counts(), exp)

# normalize
exp = Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name="xxx")
tm.assert_series_equal(ser.value_counts(normalize=True), exp)
tm.assert_series_equal(idx.value_counts(normalize=True), exp)
