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
        "C": [
            "dull",
            "dull",
            "shiny",
            "dull",
            "dull",
            "shiny",
            "shiny",
            "dull",
            "shiny",
            "shiny",
            "shiny",
        ],
        "D": np.random.randn(11),
        "E": np.random.randn(11),
        "F": np.random.randn(11),
    }
)

grouped = data.groupby(["A", "B"])
funcs = [np.mean, np.std]
with pytest.raises(TypeError, match="Could not convert dullshinyshiny to numeric"):
    grouped.agg(funcs)
