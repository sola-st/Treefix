# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
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
        "D": np.random.randn(11),
        "E": np.random.randn(11),
        "F": np.random.randn(11),
    }
)

grouped = data.groupby(["A", "B"])
funcs = [np.mean, np.std]
agged = grouped.agg(funcs)
expected = pd.concat(
    [grouped["D"].agg(funcs), grouped["E"].agg(funcs), grouped["F"].agg(funcs)],
    keys=["D", "E", "F"],
    axis=1,
)
assert isinstance(agged.index, MultiIndex)
assert isinstance(expected.index, MultiIndex)
tm.assert_frame_equal(agged, expected)
