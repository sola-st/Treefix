# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH#38642
df = DataFrame(
    {
        "key": Categorical(["b", "b", "a"], categories=["a", "b", "c"]),
        "col": range(3),
    }
)
grouped = df.groupby("key", sort=False)
result = grouped.indices
expected = {
    "b": np.array([0, 1], dtype="intp"),
    "a": np.array([2], dtype="intp"),
    "c": np.array([], dtype="intp"),
}
assert result.keys() == expected.keys()
for key in result.keys():
    tm.assert_numpy_array_equal(result[key], expected[key])
