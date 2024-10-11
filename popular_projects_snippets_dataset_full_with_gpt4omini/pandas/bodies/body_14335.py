# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:
    store["a"] = tm.makeTimeSeries()
    store["b"] = tm.makeDataFrame()
    df = tm.makeTimeDataFrame()
    _maybe_remove(store, "df1")
    store.append("df1", df[:10])
    store.append("df1", df[10:])
    assert store.root.a._v_attrs.pandas_version == "0.15.2"
    assert store.root.b._v_attrs.pandas_version == "0.15.2"
    assert store.root.df1._v_attrs.pandas_version == "0.15.2"

    # write a file and wipe its versioning
    _maybe_remove(store, "df2")
    store.append("df2", df)

    # this is an error because its table_type is appendable, but no
    # version info
    store.get_node("df2")._v_attrs.pandas_version = None

    msg = "'NoneType' object has no attribute 'startswith'"

    with pytest.raises(Exception, match=msg):
        store.select("df2")
