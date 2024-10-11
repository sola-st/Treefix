# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#47209 test adding array of ints when freq.n > 1 matches
#  scalar behavior
pi = period_range("2016-01-01", periods=10, freq="2D")
arr = np.arange(10)
result = pi + arr
expected = pd.Index([x + y for x, y in zip(pi, arr)])
tm.assert_index_equal(result, expected)

result = pi - arr
expected = pd.Index([x - y for x, y in zip(pi, arr)])
tm.assert_index_equal(result, expected)
