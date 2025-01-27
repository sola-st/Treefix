# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 23309
# see test_interval_tree.py for extensive tests; interface tests here

# non-overlapping
tuples = [(start + n * shift, start + (n + 1) * shift) for n in (0, 2, 4)]
index = IntervalIndex.from_tuples(tuples, closed=closed)
assert index.is_overlapping is False

# non-overlapping with NA
tuples = [(na_value, na_value)] + tuples + [(na_value, na_value)]
index = IntervalIndex.from_tuples(tuples, closed=closed)
assert index.is_overlapping is False

# overlapping
tuples = [(start + n * shift, start + (n + 2) * shift) for n in range(3)]
index = IntervalIndex.from_tuples(tuples, closed=closed)
assert index.is_overlapping is True

# overlapping with NA
tuples = [(na_value, na_value)] + tuples + [(na_value, na_value)]
index = IntervalIndex.from_tuples(tuples, closed=closed)
assert index.is_overlapping is True

# common endpoints
tuples = [(start + n * shift, start + (n + 1) * shift) for n in range(3)]
index = IntervalIndex.from_tuples(tuples, closed=closed)
result = index.is_overlapping
expected = closed == "both"
assert result is expected

# common endpoints with NA
tuples = [(na_value, na_value)] + tuples + [(na_value, na_value)]
index = IntervalIndex.from_tuples(tuples, closed=closed)
result = index.is_overlapping
assert result is expected

# intervals with duplicate left values
a = [10, 15, 20, 25, 30, 35, 40, 45, 45, 50, 55, 60, 65, 70, 75, 80, 85]
b = [15, 20, 25, 30, 35, 40, 45, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
index = IntervalIndex.from_arrays(a, b, closed="right")
result = index.is_overlapping
assert result is False
