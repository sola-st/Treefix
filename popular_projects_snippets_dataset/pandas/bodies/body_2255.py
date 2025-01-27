# Extracted from ./data/repos/pandas/pandas/tests/frame/test_npfuncs.py
df = DataFrame({"A": Categorical([1, 2]), "B": Categorical([1, 2])})
result = np.asarray(df)
# may change from object in the future
expected = np.array([[1, 1], [2, 2]], dtype="object")
tm.assert_numpy_array_equal(result, expected)
