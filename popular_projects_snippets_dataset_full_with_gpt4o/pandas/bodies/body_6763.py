# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 20636
index = IntervalIndex.from_breaks(breaks)

# intervalindex
result = index._maybe_convert_i8(index)
expected = IntervalIndex.from_breaks(breaks.asi8)
tm.assert_index_equal(result, expected)

# interval
interval = Interval(breaks[0], breaks[1])
result = index._maybe_convert_i8(interval)
expected = Interval(breaks[0].value, breaks[1].value)
assert result == expected

# datetimelike index
result = index._maybe_convert_i8(breaks)
expected = Index(breaks.asi8)
tm.assert_index_equal(result, expected)

# datetimelike scalar
result = index._maybe_convert_i8(breaks[0])
expected = breaks[0].value
assert result == expected

# list-like of datetimelike scalars
result = index._maybe_convert_i8(list(breaks))
expected = Index(breaks.asi8)
tm.assert_index_equal(result, expected)
