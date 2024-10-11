# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py

# default_format option
with ensure_clean_store(setup_path) as store:
    df = tm.makeDataFrame()

    with pd.option_context("io.hdf.default_format", "fixed"):
        _maybe_remove(store, "df")
        store.put("df", df)
        assert not store.get_storer("df").is_table

        msg = "Can only append to Tables"
        with pytest.raises(ValueError, match=msg):
            store.append("df2", df)

    with pd.option_context("io.hdf.default_format", "table"):
        _maybe_remove(store, "df")
        store.put("df", df)
        assert store.get_storer("df").is_table

        _maybe_remove(store, "df2")
        store.append("df2", df)
        assert store.get_storer("df").is_table

path = tmp_path / setup_path
df = tm.makeDataFrame()

with pd.option_context("io.hdf.default_format", "fixed"):
    df.to_hdf(path, "df")
    with HDFStore(path) as store:
        assert not store.get_storer("df").is_table
    with pytest.raises(ValueError, match=msg):
        df.to_hdf(path, "df2", append=True)

with pd.option_context("io.hdf.default_format", "table"):
    df.to_hdf(path, "df3")
    with HDFStore(path) as store:
        assert store.get_storer("df3").is_table
    df.to_hdf(path, "df4", append=True)
    with HDFStore(path) as store:
        assert store.get_storer("df4").is_table
