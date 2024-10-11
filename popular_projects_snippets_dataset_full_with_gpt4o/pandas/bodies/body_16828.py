# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
left = DataFrame({"key": ["foo", "bar", "baz", "foo"], "value": [1, 2, 3, 4]})
right = DataFrame({"value2": ["a", "b", "c"]}, index=["bar", "baz", "foo"])

joined = left.join(right, on="key", sort=True)
expected = DataFrame(
    {
        "key": ["bar", "baz", "foo", "foo"],
        "value": [2, 3, 1, 4],
        "value2": ["a", "b", "c", "c"],
    },
    index=[1, 2, 0, 3],
)
tm.assert_frame_equal(joined, expected)

# smoke test
joined = left.join(right, on="key", sort=False)
tm.assert_index_equal(joined.index, Index(range(4)), exact=True)
