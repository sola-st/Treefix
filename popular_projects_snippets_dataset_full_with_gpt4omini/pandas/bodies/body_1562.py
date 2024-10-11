# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 34870

index = MultiIndex.from_tuples(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    ),
    names=["first", "second"],
)

result = Series([1, 1, 1, 1, 1, 1, 1, 1], index=index)
result.loc[("baz", "one"):("foo", "two")] = 100

expected = Series([1, 1, 100, 100, 100, 100, 1, 1], index=index)

tm.assert_series_equal(result, expected)
