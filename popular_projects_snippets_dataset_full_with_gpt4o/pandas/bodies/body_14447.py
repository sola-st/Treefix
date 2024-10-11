# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

# GH 8014
# using iterator and where clause can return many empty
# frames.
chunksize = 10_000

# with iterator, range limited to the first chunk
with ensure_clean_store(setup_path) as store:

    expected = tm.makeTimeDataFrame(100000, "S")
    _maybe_remove(store, "df")
    store.append("df", expected)

    beg_dt = expected.index[0]
    end_dt = expected.index[chunksize - 1]

    # select w/iterator and where clause, single term, begin of range
    where = f"index >= '{beg_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    result = concat(results)
    rexpected = expected[expected.index >= beg_dt]
    tm.assert_frame_equal(rexpected, result)

    # select w/iterator and where clause, single term, end of range
    where = f"index <= '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))

    assert len(results) == 1
    result = concat(results)
    rexpected = expected[expected.index <= end_dt]
    tm.assert_frame_equal(rexpected, result)

    # select w/iterator and where clause, inclusive range
    where = f"index >= '{beg_dt}' & index <= '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))

    # should be 1, is 10
    assert len(results) == 1
    result = concat(results)
    rexpected = expected[(expected.index >= beg_dt) & (expected.index <= end_dt)]
    tm.assert_frame_equal(rexpected, result)

    # select w/iterator and where clause which selects
    # *nothing*.
    #
    # To be consistent with Python idiom I suggest this should
    # return [] e.g. `for e in []: print True` never prints
    # True.

    where = f"index <= '{beg_dt}' & index >= '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))

    # should be []
    assert len(results) == 0
