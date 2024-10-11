# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

# GH 8014
# using iterator and where clause
chunksize = 1e4

# no iterator
with ensure_clean_store(setup_path) as store:

    expected = tm.makeTimeDataFrame(100064, "S")
    _maybe_remove(store, "df")
    store.append("df", expected)

    beg_dt = expected.index[0]
    end_dt = expected.index[-1]

    # select w/o iteration and no where clause works
    result = store.select("df")
    tm.assert_frame_equal(expected, result)

    # select w/o iterator and where clause, single term, begin
    # of range, works
    where = f"index >= '{beg_dt}'"
    result = store.select("df", where=where)
    tm.assert_frame_equal(expected, result)

    # select w/o iterator and where clause, single term, end
    # of range, works
    where = f"index <= '{end_dt}'"
    result = store.select("df", where=where)
    tm.assert_frame_equal(expected, result)

    # select w/o iterator and where clause, inclusive range,
    # works
    where = f"index >= '{beg_dt}' & index <= '{end_dt}'"
    result = store.select("df", where=where)
    tm.assert_frame_equal(expected, result)

# with iterator, full range
with ensure_clean_store(setup_path) as store:

    expected = tm.makeTimeDataFrame(100064, "S")
    _maybe_remove(store, "df")
    store.append("df", expected)

    beg_dt = expected.index[0]
    end_dt = expected.index[-1]

    # select w/iterator and no where clause works
    results = list(store.select("df", chunksize=chunksize))
    result = concat(results)
    tm.assert_frame_equal(expected, result)

    # select w/iterator and where clause, single term, begin of range
    where = f"index >= '{beg_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    result = concat(results)
    tm.assert_frame_equal(expected, result)

    # select w/iterator and where clause, single term, end of range
    where = f"index <= '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    result = concat(results)
    tm.assert_frame_equal(expected, result)

    # select w/iterator and where clause, inclusive range
    where = f"index >= '{beg_dt}' & index <= '{end_dt}'"
    results = list(store.select("df", where=where, chunksize=chunksize))
    result = concat(results)
    tm.assert_frame_equal(expected, result)
