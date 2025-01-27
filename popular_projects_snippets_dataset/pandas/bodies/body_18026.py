# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
result1 = hash_array(np.array(["3", "4", "All"]))
result2 = hash_array(np.array([3, 4, "All"], dtype=dtype))

tm.assert_numpy_array_equal(result1, result2)
