# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py
# GH-12007
# test fix for when concat on categorical and float
# coerces dtype categorical -> float
df = DataFrame(Series(["a", "b", "c"], dtype="category", name="A"))
ser = Series([0, 1, 2], index=[0, 1, 3], name="B")
result = pd.concat([df, ser], axis=1)
expected = DataFrame(
    {
        "A": Series(["a", "b", "c", np.nan], dtype="category"),
        "B": Series([0, 1, np.nan, 2], dtype="float"),
    }
)
tm.assert_equal(result, expected)
