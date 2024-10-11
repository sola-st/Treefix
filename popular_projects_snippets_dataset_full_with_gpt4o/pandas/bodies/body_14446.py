# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

# GH 8014
# using iterator and where clause
chunksize = 1e4

# with iterator, non complete range
with ensure_clean_store(setup_path) as store:

    expected = tm.makeTimeDataFrame(100064, "S")
    _maybe_remove(store, "df")
    store.append("df", expected)

    beg_dt = expected.index[1]
    end_dt = expected.index[-2]

    # select w/iterator and where clause, single term, begin of range
    where = f"index >= '{beg_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    result = concat(results)
    rexpected = expected[expected.index >= beg_dt]
    tm.assert_frame_equal(rexpected, result)

    # select w/iterator and where clause, single term, end of range
    where = f"index <= '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    result = concat(results)
    rexpected = expected[expected.index <= end_dt]
    tm.assert_frame_equal(rexpected, result)

    # select w/iterator and where clause, inclusive range
    where = f"index >= '{beg_dt}' & index <= '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    result = concat(results)
    rexpected = expected[(expected.index >= beg_dt) & (expected.index <= end_dt)]
    tm.assert_frame_equal(rexpected, result)

# with iterator, empty where
with ensure_clean_store(setup_path) as store:

    expected = tm.makeTimeDataFrame(100064, "S")
    _maybe_remove(store, "df")
    store.append("df", expected)

    end_dt = expected.index[-1]

    # select w/iterator and where clause, single term, begin of range
    where = f"index > '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    assert 0 == len(results)
