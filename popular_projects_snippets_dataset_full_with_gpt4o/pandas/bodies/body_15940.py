# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
# GH#16934

# Set up a Series with a three level MultiIndex
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
    [4, 3, 2, 1, 4, 3, 2, 1],
]
tuples = zip(*arrays)
mi = MultiIndex.from_tuples(tuples, names=["first", "second", "third"])
ser = Series(range(8), index=mi)

# Sort with boolean ascending
result = ser.sort_index(level=["third", "first"], ascending=False)
expected = ser.iloc[[4, 0, 5, 1, 6, 2, 7, 3]]
tm.assert_series_equal(result, expected)

# Sort with list of boolean ascending
result = ser.sort_index(level=["third", "first"], ascending=[False, True])
expected = ser.iloc[[0, 4, 1, 5, 2, 6, 3, 7]]
tm.assert_series_equal(result, expected)
