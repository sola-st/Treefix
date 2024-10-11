# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# same as above, but for Integer based indexes
# these coerce to a like integer
# oob indicates if we are out of bounds
# of positional indexing
for index, oob in [
    (NumericIndex(np.arange(5, dtype=np.int64)), False),
    (RangeIndex(5), False),
    (NumericIndex(np.arange(5, dtype=np.int64) + 10), True),
]:

    # s is an in-range index
    s = Series(range(5), index=index)

    # getitem
    for idx in [slice(3.0, 4), slice(3, 4.0), slice(3.0, 4.0)]:

        result = s.loc[idx]

        # these are all label indexing
        # except getitem which is positional
        # empty
        if oob:
            indexer = slice(0, 0)
        else:
            indexer = slice(3, 5)
        self.check(result, s, indexer, False)

    # getitem out-of-bounds
    for idx in [slice(-6, 6), slice(-6.0, 6.0)]:

        result = s.loc[idx]

        # these are all label indexing
        # except getitem which is positional
        # empty
        if oob:
            indexer = slice(0, 0)
        else:
            indexer = slice(-6, 6)
        self.check(result, s, indexer, False)

    # positional indexing
    msg = (
        "cannot do slice indexing "
        rf"on {type(index).__name__} with these indexers \[-6\.0\] of "
        "type float"
    )
    with pytest.raises(TypeError, match=msg):
        s[slice(-6.0, 6.0)]

    # getitem odd floats
    for idx, res1 in [
        (slice(2.5, 4), slice(3, 5)),
        (slice(2, 3.5), slice(2, 4)),
        (slice(2.5, 3.5), slice(3, 4)),
    ]:

        result = s.loc[idx]
        if oob:
            res = slice(0, 0)
        else:
            res = res1

        self.check(result, s, res, False)

        # positional indexing
        msg = (
            "cannot do slice indexing "
            rf"on {type(index).__name__} with these indexers \[(2|3)\.5\] of "
            "type float"
        )
        with pytest.raises(TypeError, match=msg):
            s[idx]
