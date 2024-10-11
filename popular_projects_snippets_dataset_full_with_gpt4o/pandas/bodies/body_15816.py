# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# with keywords
lst = ["a", "b", "c", "a"]
ser = Series(lst)
exp = Series(Categorical(lst, ordered=True))
res = ser.astype(CategoricalDtype(None, ordered=True))
tm.assert_series_equal(res, exp)

exp = Series(Categorical(lst, categories=list("abcdef"), ordered=True))
res = ser.astype(CategoricalDtype(list("abcdef"), ordered=True))
tm.assert_series_equal(res, exp)
