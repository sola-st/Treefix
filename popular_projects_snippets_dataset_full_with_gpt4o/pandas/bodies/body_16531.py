# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 27500
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
# normalize on index
result = crosstab(
    [df.A, df.B], df.C, margins=True, margins_name="Sub-Total", normalize=0
)
expected = DataFrame(
    [[0.5, 0.5], [0.5, 0.5], [0.666667, 0.333333], [0, 1], [0.444444, 0.555556]]
)
expected.index = MultiIndex(
    levels=[["Sub-Total", "bar", "foo"], ["", "one", "two"]],
    codes=[[1, 1, 2, 2, 0], [1, 2, 1, 2, 0]],
    names=["A", "B"],
)
expected.columns = Index(["large", "small"], dtype="object", name="C")
tm.assert_frame_equal(result, expected)

# normalize on columns
result = crosstab(
    [df.A, df.B], df.C, margins=True, margins_name="Sub-Total", normalize=1
)
expected = DataFrame(
    [
        [0.25, 0.2, 0.222222],
        [0.25, 0.2, 0.222222],
        [0.5, 0.2, 0.333333],
        [0, 0.4, 0.222222],
    ]
)
expected.columns = Index(
    ["large", "small", "Sub-Total"], dtype="object", name="C"
)
expected.index = MultiIndex(
    levels=[["bar", "foo"], ["one", "two"]],
    codes=[[0, 0, 1, 1], [0, 1, 0, 1]],
    names=["A", "B"],
)
tm.assert_frame_equal(result, expected)

# normalize on both index and column
result = crosstab(
    [df.A, df.B], df.C, margins=True, margins_name="Sub-Total", normalize=True
)
expected = DataFrame(
    [
        [0.111111, 0.111111, 0.222222],
        [0.111111, 0.111111, 0.222222],
        [0.222222, 0.111111, 0.333333],
        [0.000000, 0.222222, 0.222222],
        [0.444444, 0.555555, 1],
    ]
)
expected.columns = Index(
    ["large", "small", "Sub-Total"], dtype="object", name="C"
)
expected.index = MultiIndex(
    levels=[["Sub-Total", "bar", "foo"], ["", "one", "two"]],
    codes=[[1, 1, 2, 2, 0], [1, 2, 1, 2, 0]],
    names=["A", "B"],
)
tm.assert_frame_equal(result, expected)
