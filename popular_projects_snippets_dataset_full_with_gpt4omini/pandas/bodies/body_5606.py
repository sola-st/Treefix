# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 20866
arr = np.array(["foo", None], dtype=object)
result = pd.unique(arr)
expected = np.array(["foo", None], dtype=object)

tm.assert_numpy_array_equal(result, expected, strict_nan=True)
