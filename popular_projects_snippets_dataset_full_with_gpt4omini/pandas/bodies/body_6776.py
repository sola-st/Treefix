# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py

index1 = IntervalIndex.from_arrays([0, 1], [1, 2], closed=closed)
index2 = IntervalIndex.from_arrays([1, 2], [2, 3], closed=closed)

result = index1.append(index2)
expected = IntervalIndex.from_arrays([0, 1, 1, 2], [1, 2, 2, 3], closed=closed)
tm.assert_index_equal(result, expected)

result = index1.append([index1, index2])
expected = IntervalIndex.from_arrays(
    [0, 1, 0, 1, 1, 2], [1, 2, 1, 2, 2, 3], closed=closed
)
tm.assert_index_equal(result, expected)

for other_closed in {"left", "right", "both", "neither"} - {closed}:
    index_other_closed = IntervalIndex.from_arrays(
        [0, 1], [1, 2], closed=other_closed
    )
    result = index1.append(index_other_closed)
    expected = index1.astype(object).append(index_other_closed.astype(object))
    tm.assert_index_equal(result, expected)
