# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
start, stop = query
index = IntervalIndex.from_tuples(tuples)
with pytest.raises(
    KeyError,
    match=(
        "'can only get slices from an IntervalIndex if bounds are "
        "non-overlapping and all monotonic increasing or decreasing'"
    ),
):
    index.slice_locs(start, stop)
