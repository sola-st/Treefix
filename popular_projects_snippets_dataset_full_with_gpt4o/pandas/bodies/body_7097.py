# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py

# GH11193, when an existing index is passed, and a new name is not
# specified, the new index should inherit the previous object name
expected = simple_index
if not isinstance(expected, MultiIndex):
    expected.name = "foo"
    result = Index(expected)
    tm.assert_index_equal(result, expected)

    result = Index(expected, name="bar")
    expected.name = "bar"
    tm.assert_index_equal(result, expected)
else:
    expected.names = ["foo", "bar"]
    result = Index(expected)
    tm.assert_index_equal(
        result,
        Index(
            Index(
                [
                    ("foo", "one"),
                    ("foo", "two"),
                    ("bar", "one"),
                    ("baz", "two"),
                    ("qux", "one"),
                    ("qux", "two"),
                ],
                dtype="object",
            ),
            names=["foo", "bar"],
        ),
    )

    result = Index(expected, names=["A", "B"])
    tm.assert_index_equal(
        result,
        Index(
            Index(
                [
                    ("foo", "one"),
                    ("foo", "two"),
                    ("bar", "one"),
                    ("baz", "two"),
                    ("qux", "one"),
                    ("qux", "two"),
                ],
                dtype="object",
            ),
            names=["A", "B"],
        ),
    )
