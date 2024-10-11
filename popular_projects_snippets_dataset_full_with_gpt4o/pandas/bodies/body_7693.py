# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py

# GH11193, when an existing index is passed, and a new name is not
# specified, the new index should inherit the previous object name
index = idx
index.names = ["foo", "bar"]
result = Index(index)
expected = Index(
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
    )
)
tm.assert_index_equal(result, expected)

result = Index(index, name="A")
expected = Index(
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
    name="A",
)
tm.assert_index_equal(result, expected)
