# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

df = DataFrame(np.random.rand(3, 3), columns=list("ABC"), index=list("aab"))

result = df.iloc[0]
assert isinstance(result, Series)
tm.assert_almost_equal(result.values, df.values[0])

result = df.T.iloc[:, 0]
assert isinstance(result, Series)
tm.assert_almost_equal(result.values, df.values[0])
