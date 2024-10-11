# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 7856
df = DataFrame(
    [
        {
            "a": "foo",
            "b": "bar",
            "c": "uncomfortably long line with lots of stuff",
            "d": 1,
        },
        {"a": "foo", "b": "bar", "c": "stuff", "d": 1},
    ]
)
df.set_index(["a", "b", "c"])
assert str(df) == (
    "     a    b                                           c  d\n"
    "0  foo  bar  uncomfortably long line with lots of stuff  1\n"
    "1  foo  bar                                       stuff  1"
)
with option_context("max_colwidth", 20):
    assert str(df) == (
        "     a    b                    c  d\n"
        "0  foo  bar  uncomfortably lo...  1\n"
        "1  foo  bar                stuff  1"
    )
