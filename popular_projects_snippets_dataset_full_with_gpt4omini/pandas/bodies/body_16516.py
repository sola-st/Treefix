# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py

df = DataFrame(
    {"a": [1, np.nan, np.nan, np.nan, np.nan, 2], "b": [3, 3, 4, 4, 4, 4]}
)
actual = crosstab(df.a, df.b, margins=True, dropna=True)
expected = DataFrame([[1, 0, 1], [0, 1, 1], [1, 1, 2]])
expected.index = Index([1.0, 2.0, "All"], name="a")
expected.columns = Index([3, 4, "All"], name="b")
tm.assert_frame_equal(actual, expected)
