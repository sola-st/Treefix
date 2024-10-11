# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
c = Categorical(list("ABABC"), categories=list("CBA"), ordered=True)
result = c.map(lambda x: x.lower())
exp = Categorical(list("ababc"), categories=list("cba"), ordered=True)
tm.assert_categorical_equal(result, exp)

c = Categorical(list("ABABC"), categories=list("ABC"), ordered=False)
result = c.map(lambda x: x.lower())
exp = Categorical(list("ababc"), categories=list("abc"), ordered=False)
tm.assert_categorical_equal(result, exp)

result = c.map(lambda x: 1)
# GH 12766: Return an index not an array
tm.assert_index_equal(result, Index(np.array([1] * 5, dtype=np.int64)))
