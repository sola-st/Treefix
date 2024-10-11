# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
a = np.array(["foo", "foo", "foo", "bar", "bar", "foo", "foo"], dtype=object)
b = np.array(["one", "one", "two", "one", "two", np.nan, "two"], dtype=object)
c = np.array(
    ["dull", "dull", "dull", "dull", "dull", "shiny", "shiny"], dtype=object
)

actual = crosstab(
    a, [b, c], rownames=["a"], colnames=["b", "c"], margins=True, dropna=False
)
m = MultiIndex.from_arrays(
    [
        ["one", "one", "two", "two", "All"],
        ["dull", "shiny", "dull", "shiny", ""],
    ],
    names=["b", "c"],
)
expected = DataFrame(
    [[1, 0, 1, 0, 2], [2, 0, 1, 1, 5], [3, 0, 2, 1, 7]], columns=m
)
expected.index = Index(["bar", "foo", "All"], name="a")
tm.assert_frame_equal(actual, expected)

actual = crosstab(
    [a, b], c, rownames=["a", "b"], colnames=["c"], margins=True, dropna=False
)
m = MultiIndex.from_arrays(
    [["bar", "bar", "foo", "foo", "All"], ["one", "two", "one", "two", ""]],
    names=["a", "b"],
)
expected = DataFrame(
    [[1, 0, 1], [1, 0, 1], [2, 0, 2], [1, 1, 2], [5, 2, 7]], index=m
)
expected.columns = Index(["dull", "shiny", "All"], name="c")
tm.assert_frame_equal(actual, expected)

actual = crosstab(
    [a, b], c, rownames=["a", "b"], colnames=["c"], margins=True, dropna=True
)
m = MultiIndex.from_arrays(
    [["bar", "bar", "foo", "foo", "All"], ["one", "two", "one", "two", ""]],
    names=["a", "b"],
)
expected = DataFrame(
    [[1, 0, 1], [1, 0, 1], [2, 0, 2], [1, 1, 2], [5, 1, 6]], index=m
)
expected.columns = Index(["dull", "shiny", "All"], name="c")
tm.assert_frame_equal(actual, expected)
