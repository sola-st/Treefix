# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py

with ensure_clean_store(setup_path) as store:

    ts = tm.makeTimeSeries()
    df = tm.makeTimeDataFrame()
    store["a"] = ts
    store["b"] = df[:10]
    store["foo/bar/bah"] = df[:10]
    store["foo"] = df[:10]
    store["/foo"] = df[:10]
    store.put("c", df[:10], format="table")

    # not OK, not a table
    msg = "Can only append to Tables"
    with pytest.raises(ValueError, match=msg):
        store.put("b", df[10:], append=True)

    # node does not currently exist, test _is_table_type returns False
    # in this case
    _maybe_remove(store, "f")
    with pytest.raises(ValueError, match=msg):
        store.put("f", df[10:], append=True)

    # can't put to a table (use append instead)
    with pytest.raises(ValueError, match=msg):
        store.put("c", df[10:], append=True)

    # overwrite table
    store.put("c", df[:10], format="table", append=False)
    tm.assert_frame_equal(df[:10], store["c"])
