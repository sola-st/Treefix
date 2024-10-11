# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
expected = DataFrame(
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

result = expected.apply(lambda x: x, axis=1)
tm.assert_frame_equal(result, expected)
