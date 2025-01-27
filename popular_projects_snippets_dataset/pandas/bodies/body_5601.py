# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
duplicated_items = ["a", np.nan, "c", "c"]
result = pd.unique(duplicated_items)
expected = np.array(["a", np.nan, "c"], dtype=object)
tm.assert_numpy_array_equal(result, expected)
