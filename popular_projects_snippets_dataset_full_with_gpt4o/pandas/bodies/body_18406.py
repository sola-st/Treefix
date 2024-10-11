# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
# IntervalIndex/Series that rely on IntervalArray for comparisons
breaks = range(4)
index = constructor(IntervalIndex.from_breaks(breaks))

# scalar comparisons
other = index[0]
result = op(index, other)
expected = expected_type(self.elementwise_comparison(op, index, other))
assert_func(result, expected)

other = breaks[0]
result = op(index, other)
expected = expected_type(self.elementwise_comparison(op, index, other))
assert_func(result, expected)

# list-like comparisons
other = IntervalArray.from_breaks(breaks)
result = op(index, other)
expected = expected_type(self.elementwise_comparison(op, index, other))
assert_func(result, expected)

other = [index[0], breaks[0], "foo"]
result = op(index, other)
expected = expected_type(self.elementwise_comparison(op, index, other))
assert_func(result, expected)
