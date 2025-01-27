# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list("ABC"))
df = DataFrame([[1, 2], [3, 4]], mi)

result = df.sort_index(level="A", sort_remaining=False)
expected = df
tm.assert_frame_equal(result, expected)

result = df.sort_index(level=["A", "B"], sort_remaining=False)
expected = df
tm.assert_frame_equal(result, expected)

# Error thrown by sort_index when
# first index is sorted last (GH#26053)
result = df.sort_index(level=["C", "B", "A"])
expected = df.iloc[[1, 0]]
tm.assert_frame_equal(result, expected)

result = df.sort_index(level=["B", "C", "A"])
expected = df.iloc[[1, 0]]
tm.assert_frame_equal(result, expected)

result = df.sort_index(level=["C", "A"])
expected = df.iloc[[1, 0]]
tm.assert_frame_equal(result, expected)
