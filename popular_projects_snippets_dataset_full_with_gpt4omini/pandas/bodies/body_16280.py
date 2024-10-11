# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 26336: the string 'category' maintains existing CategoricalDtype
cdt = CategoricalDtype(categories=list("dabc"), ordered=True)
expected = Series(list("abcabc"), dtype=cdt)

# Series(Categorical, dtype='category') keeps existing dtype
cat = Categorical(list("abcabc"), dtype=cdt)
result = Series(cat, dtype="category")
tm.assert_series_equal(result, expected)

# Series(Series[Categorical], dtype='category') keeps existing dtype
result = Series(result, dtype="category")
tm.assert_series_equal(result, expected)
