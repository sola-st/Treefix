# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 35144
# use multiple columns with margins and normalization
df = DataFrame(
    {
        "A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"],
        "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"],
        "C": [
            "small",
            "large",
            "large",
            "small",
            "small",
            "large",
            "small",
            "small",
            "large",
        ],
        "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
        "E": [2, 4, 5, 5, 6, 6, 8, 9, 9],
    }
)
result = crosstab(
    index=df.C,
    columns=[df.A, df.B],
    margins=True,
    margins_name="margin",
    normalize=True,
)
expected = DataFrame(
    [
        [0.111111, 0.111111, 0.222222, 0.000000, 0.444444],
        [0.111111, 0.111111, 0.111111, 0.222222, 0.555556],
        [0.222222, 0.222222, 0.333333, 0.222222, 1.0],
    ],
    index=["large", "small", "margin"],
)
expected.columns = MultiIndex(
    levels=[["bar", "foo", "margin"], ["", "one", "two"]],
    codes=[[0, 0, 1, 1, 2], [1, 2, 1, 2, 0]],
    names=["A", "B"],
)
expected.index.name = "C"
tm.assert_frame_equal(result, expected)
