# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py

idx = IntervalIndex.from_tuples([(0, 1), (2, 3)], closed=closed)

for bound in [[0, 1], [1, 2], [2, 3], [3, 4], [0, 2], [2.5, 3], [-1, 4]]:
    # if get_loc is supplied an interval, it should only search
    # for exact matches, not overlaps or covers, else KeyError.
    msg = re.escape(f"Interval({bound[0]}, {bound[1]}, closed='{side}')")
    if closed == side:
        if bound == [0, 1]:
            assert idx.get_loc(Interval(0, 1, closed=side)) == 0
        elif bound == [2, 3]:
            assert idx.get_loc(Interval(2, 3, closed=side)) == 1
        else:
            with pytest.raises(KeyError, match=msg):
                idx.get_loc(Interval(*bound, closed=side))
    else:
        with pytest.raises(KeyError, match=msg):
            idx.get_loc(Interval(*bound, closed=side))
