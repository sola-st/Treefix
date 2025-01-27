# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
# GH 9784 - dont truncate when calling DataFrame.to_string
df = DataFrame(
    [
        {
            "a": "foo",
            "b": "bar",
            "c": "let's make this a very VERY long line that is longer "
            "than the default 50 character limit",
            "d": 1,
        },
        {"a": "foo", "b": "bar", "c": "stuff", "d": 1},
    ]
)
df.set_index(["a", "b", "c"])
assert df.to_string() == (
    "     a    b                                         "
    "                                                c  d\n"
    "0  foo  bar  let's make this a very VERY long line t"
    "hat is longer than the default 50 character limit  1\n"
    "1  foo  bar                                         "
    "                                            stuff  1"
)
with option_context("max_colwidth", 20):
    # the display option has no effect on the to_string method
    assert df.to_string() == (
        "     a    b                                         "
        "                                                c  d\n"
        "0  foo  bar  let's make this a very VERY long line t"
        "hat is longer than the default 50 character limit  1\n"
        "1  foo  bar                                         "
        "                                            stuff  1"
    )
assert df.to_string(max_colwidth=20) == (
    "     a    b                    c  d\n"
    "0  foo  bar  let's make this ...  1\n"
    "1  foo  bar                stuff  1"
)
