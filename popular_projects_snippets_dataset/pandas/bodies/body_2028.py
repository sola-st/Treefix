# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# pass thru
result = to_timedelta(np.array([np.timedelta64(1, "s")]))
expected = pd.Index(np.array([np.timedelta64(1, "s")]))
tm.assert_index_equal(result, expected)
