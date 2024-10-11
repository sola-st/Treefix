# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
pi = period_range("20130101", periods=5, freq="D")
cond = np.array([True, False, True, True, False])

tdnat = np.timedelta64("NaT", "ns")
expected = pd.Index([pi[0], tdnat, pi[2], pi[3], tdnat], dtype=object)
assert expected[1] is tdnat
result = pi.where(cond, tdnat)
tm.assert_index_equal(result, expected)
