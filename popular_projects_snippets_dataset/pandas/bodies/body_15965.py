# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_value_counts.py
values = Categorical([1, 2, 3, 1, 1, 3], ordered=False)

exp_idx = CategoricalIndex([1, 3, 2], categories=[1, 2, 3], ordered=False)
exp = Series([3, 2, 1], index=exp_idx, name="xxx")

ser = Series(values, name="xxx")
tm.assert_series_equal(ser.value_counts(), exp)
# check CategoricalIndex outputs the same result
idx = CategoricalIndex(values, name="xxx")
tm.assert_series_equal(idx.value_counts(), exp)

# normalize
exp = Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name="xxx")
tm.assert_series_equal(ser.value_counts(normalize=True), exp)
tm.assert_series_equal(idx.value_counts(normalize=True), exp)
