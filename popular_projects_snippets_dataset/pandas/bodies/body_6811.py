# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py

# increasing monotonically
index = IntervalIndex.from_tuples([(0, 2), (1, 3), (2, 4)])

assert index.slice_locs(start=Interval(0, 2), end=Interval(2, 4)) == (0, 3)
assert index.slice_locs(start=Interval(0, 2)) == (0, 3)
assert index.slice_locs(end=Interval(2, 4)) == (0, 3)
assert index.slice_locs(end=Interval(0, 2)) == (0, 1)
assert index.slice_locs(start=Interval(2, 4), end=Interval(0, 2)) == (2, 1)

# decreasing monotonically
index = IntervalIndex.from_tuples([(2, 4), (1, 3), (0, 2)])

assert index.slice_locs(start=Interval(0, 2), end=Interval(2, 4)) == (2, 1)
assert index.slice_locs(start=Interval(0, 2)) == (2, 3)
assert index.slice_locs(end=Interval(2, 4)) == (0, 1)
assert index.slice_locs(end=Interval(0, 2)) == (0, 3)
assert index.slice_locs(start=Interval(2, 4), end=Interval(0, 2)) == (0, 3)

# sorted duplicates
index = IntervalIndex.from_tuples([(0, 2), (0, 2), (2, 4)])

assert index.slice_locs(start=Interval(0, 2), end=Interval(2, 4)) == (0, 3)
assert index.slice_locs(start=Interval(0, 2)) == (0, 3)
assert index.slice_locs(end=Interval(2, 4)) == (0, 3)
assert index.slice_locs(end=Interval(0, 2)) == (0, 2)
assert index.slice_locs(start=Interval(2, 4), end=Interval(0, 2)) == (2, 2)

# unsorted duplicates
index = IntervalIndex.from_tuples([(0, 2), (2, 4), (0, 2)])

with pytest.raises(
    KeyError,
    match=re.escape(
        '"Cannot get left slice bound for non-unique label: '
        "Interval(0, 2, closed='right')\""
    ),
):
    index.slice_locs(start=Interval(0, 2), end=Interval(2, 4))

with pytest.raises(
    KeyError,
    match=re.escape(
        '"Cannot get left slice bound for non-unique label: '
        "Interval(0, 2, closed='right')\""
    ),
):
    index.slice_locs(start=Interval(0, 2))

assert index.slice_locs(end=Interval(2, 4)) == (0, 2)

with pytest.raises(
    KeyError,
    match=re.escape(
        '"Cannot get right slice bound for non-unique label: '
        "Interval(0, 2, closed='right')\""
    ),
):
    index.slice_locs(end=Interval(0, 2))

with pytest.raises(
    KeyError,
    match=re.escape(
        '"Cannot get right slice bound for non-unique label: '
        "Interval(0, 2, closed='right')\""
    ),
):
    index.slice_locs(start=Interval(2, 4), end=Interval(0, 2))

# another unsorted duplicates
index = IntervalIndex.from_tuples([(0, 2), (0, 2), (2, 4), (1, 3)])

assert index.slice_locs(start=Interval(0, 2), end=Interval(2, 4)) == (0, 3)
assert index.slice_locs(start=Interval(0, 2)) == (0, 4)
assert index.slice_locs(end=Interval(2, 4)) == (0, 3)
assert index.slice_locs(end=Interval(0, 2)) == (0, 2)
assert index.slice_locs(start=Interval(2, 4), end=Interval(0, 2)) == (2, 2)
