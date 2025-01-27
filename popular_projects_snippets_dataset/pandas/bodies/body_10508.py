# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
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

def bad(x):
    assert len(x.values.base) > 0
    exit("foo")

result = data.groupby(["A", "B"]).agg(bad)
expected = data.groupby(["A", "B"]).agg(lambda x: "foo")
tm.assert_frame_equal(result, expected)
