# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH #18713
# for correctness purposes
data = DataFrame(
    {
        "A": [
            "foo",
            "foo",
            "foo",
            "foo",
            "bar",
            "bar",
            "bar",
            "bar",
            "foo",
            "foo",
            "foo",
        ],
        "B": [
            "one",
            "one",
            "one",
            "two",
            "one",
            "one",
            "one",
            "two",
            "two",
            "two",
            "one",
        ],
        "C": range(11),
    }
)

result = pivot_table(data, index="A", columns="B", aggfunc="sum")
mi = MultiIndex(
    levels=[["C"], ["one", "two"]], codes=[[0, 0], [0, 1]], names=[None, "B"]
)
expected = DataFrame(
    {("C", "one"): {"bar": 15, "foo": 13}, ("C", "two"): {"bar": 7, "foo": 20}},
    columns=mi,
).rename_axis("A")
tm.assert_frame_equal(result, expected)

result = pivot_table(data, index="A", columns="B", aggfunc=["sum", "mean"])
mi = MultiIndex(
    levels=[["sum", "mean"], ["C"], ["one", "two"]],
    codes=[[0, 0, 1, 1], [0, 0, 0, 0], [0, 1, 0, 1]],
    names=[None, None, "B"],
)
expected = DataFrame(
    {
        ("mean", "C", "one"): {"bar": 5.0, "foo": 3.25},
        ("mean", "C", "two"): {"bar": 7.0, "foo": 6.666666666666667},
        ("sum", "C", "one"): {"bar": 15, "foo": 13},
        ("sum", "C", "two"): {"bar": 7, "foo": 20},
    },
    columns=mi,
).rename_axis("A")
tm.assert_frame_equal(result, expected)
