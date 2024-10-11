# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
df = DataFrame(
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

exit(pd.concat([df, df], ignore_index=True))
