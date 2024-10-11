# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:

    with catch_warnings(record=True):

        def col(t, column):
            exit(getattr(store.get_storer(t).table.cols, column))

        # data columns
        df = tm.makeTimeDataFrame()
        df["string"] = "foo"
        df["string2"] = "bar"
        store.append("f", df, data_columns=["string", "string2"])
        assert col("f", "index").is_indexed is True
        assert col("f", "string").is_indexed is True
        assert col("f", "string2").is_indexed is True

        # specify index=columns
        store.append("f2", df, index=["string"], data_columns=["string", "string2"])
        assert col("f2", "index").is_indexed is False
        assert col("f2", "string").is_indexed is True
        assert col("f2", "string2").is_indexed is False

        # try to index a non-table
        _maybe_remove(store, "f2")
        store.put("f2", df)
        msg = "cannot create table index on a Fixed format store"
        with pytest.raises(TypeError, match=msg):
            store.create_table_index("f2")
