# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
df = DataFrame(
    [[1, 2, "a", "b"], [1, 2, "a", "b"]], columns=["one", "one", "two", "two"]
)

result = df.values
expected = np.array([[1, 2, "a", "b"], [1, 2, "a", "b"]], dtype=object)

tm.assert_numpy_array_equal(result, expected)
