# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_value_counts.py
# GH#12835
cats = Categorical(list("abcccb"), categories=list("cabd"))
ser = Series(cats, name="xxx")
res = ser.value_counts(sort=False)

exp_index = CategoricalIndex(list("cabd"), categories=cats.categories)
exp = Series([3, 1, 2, 0], name="xxx", index=exp_index)
tm.assert_series_equal(res, exp)

res = ser.value_counts(sort=True)

exp_index = CategoricalIndex(list("cbad"), categories=cats.categories)
exp = Series([3, 2, 1, 0], name="xxx", index=exp_index)
tm.assert_series_equal(res, exp)

# check object dtype handles the Series.name as the same
# (tested in tests/base)
ser = Series(["a", "b", "c", "c", "c", "b"], name="xxx")
res = ser.value_counts()
exp = Series([3, 2, 1], name="xxx", index=["c", "b", "a"])
tm.assert_series_equal(res, exp)
