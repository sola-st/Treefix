# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
a = np.array(["2000", "2000", "2001"], dtype="datetime64[s]")
result = pd.unique(a)
expected = np.array(["2000", "2001"], dtype="datetime64[ns]")
tm.assert_numpy_array_equal(result, expected)
