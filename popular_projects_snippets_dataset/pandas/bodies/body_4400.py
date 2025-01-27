# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
expected = np.array([[4.0, 3.0, 2.0, 1.0]])
df = DataFrame(
    {"d": [4.0], "c": [3.0], "b": [2.0], "a": [1.0]},
    columns=["d", "c", "b", "a"],
)
tm.assert_numpy_array_equal(df.values, expected)
