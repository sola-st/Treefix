# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_sorted.py
arrays = [
    ["bar", "bar", "baz", "baz", "qux", "qux", "foo", "foo"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
index = index.sort_values(  # sort by third letter
    key=lambda x: x.map(lambda entry: entry[2])
)
result = DataFrame(range(8), index=index)

arrays = [
    ["foo", "foo", "bar", "bar", "qux", "qux", "baz", "baz"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
expected = DataFrame(range(8), index=index)

tm.assert_frame_equal(result, expected)
