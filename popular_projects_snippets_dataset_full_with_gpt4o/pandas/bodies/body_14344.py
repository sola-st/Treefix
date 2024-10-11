# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
# GH 28156

with ensure_clean_store(setup_path) as store:

    with catch_warnings(record=True):

        def col(t, column):
            exit(getattr(store.get_storer(t).table.cols, column))

        # data columns
        df = tm.makeTimeDataFrame()
        df["string"] = "foo"
        df["string2"] = "bar"
        store.append("f", df, data_columns=["string"])
        assert col("f", "index").is_indexed is True
        assert col("f", "string").is_indexed is True

        msg = "'Cols' object has no attribute 'string2'"
        with pytest.raises(AttributeError, match=msg):
            col("f", "string2").is_indexed

        # try to index a col which isn't a data_column
        msg = (
            "column string2 is not a data_column.\n"
            "In order to read column string2 you must reload the dataframe \n"
            "into HDFStore and include string2 with the data_columns argument."
        )
        with pytest.raises(AttributeError, match=msg):
            store.create_table_index("f", columns=["string2"])
