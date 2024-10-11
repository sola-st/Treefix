# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
with ensure_clean_store(setup_path) as store:

    # column oriented
    df = tm.makeTimeDataFrame()
    df.index = df.index._with_freq(None)  # freq doesn't round-trip

    _maybe_remove(store, "df1")
    store.append("df1", df.iloc[:, :2], axes=["columns"])
    store.append("df1", df.iloc[:, 2:])
    tm.assert_frame_equal(store["df1"], df)

    result = store.select("df1", "columns=A")
    expected = df.reindex(columns=["A"])
    tm.assert_frame_equal(expected, result)

    # selection on the non-indexable
    result = store.select("df1", ("columns=A", "index=df.index[0:4]"))
    expected = df.reindex(columns=["A"], index=df.index[0:4])
    tm.assert_frame_equal(expected, result)

    # this isn't supported
    msg = re.escape(
        "passing a filterable condition to a non-table indexer "
        "[Filter: Not Initialized]"
    )
    with pytest.raises(TypeError, match=msg):
        store.select("df1", "columns=A and index>df.index[4]")
