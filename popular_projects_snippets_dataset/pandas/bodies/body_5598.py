# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
a = np.array(["2000", "2000", "2001"], dtype="timedelta64[s]")
result = pd.unique(a)
expected = np.array([2000000000000, 2001000000000], dtype="timedelta64[ns]")
tm.assert_numpy_array_equal(result, expected)
