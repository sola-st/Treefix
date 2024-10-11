# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# Index(intervals, dtype=object) is an Index (not an IntervalIndex)
intervals = [Interval(0, 1), Interval(1, 2), Interval(2, 3)]
values = values_constructor(intervals)
result = Index(values, dtype=object)

assert type(result) is Index
tm.assert_numpy_array_equal(result.values, np.array(values))
