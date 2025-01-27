# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

# we are expecting to return in the order
# of appearance
expected = Categorical(list("bac"))

# we are expecting to return in the order
# of the categories
expected_o = Categorical(list("bac"), categories=list("abc"), ordered=True)

# GH 15939
c = Categorical(list("baabc"))
result = c.unique()
tm.assert_categorical_equal(result, expected)

result = algos.unique(c)
tm.assert_categorical_equal(result, expected)

c = Categorical(list("baabc"), ordered=True)
result = c.unique()
tm.assert_categorical_equal(result, expected_o)

result = algos.unique(c)
tm.assert_categorical_equal(result, expected_o)

# Series of categorical dtype
s = Series(Categorical(list("baabc")), name="foo")
result = s.unique()
tm.assert_categorical_equal(result, expected)

result = pd.unique(s)
tm.assert_categorical_equal(result, expected)

# CI -> return CI
ci = CategoricalIndex(Categorical(list("baabc"), categories=list("abc")))
expected = CategoricalIndex(expected)
result = ci.unique()
tm.assert_index_equal(result, expected)

result = pd.unique(ci)
tm.assert_index_equal(result, expected)
