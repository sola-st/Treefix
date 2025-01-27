# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

with ensure_clean_store(setup_path) as store:
    df = tm.makeTimeDataFrame()
    df.iloc[0, df.columns.get_loc("B")] = 1.0
    _maybe_remove(store, "df")
    store.append("df", df[:2], data_columns=["B"])
    store.append("df", df[2:])
    tm.assert_frame_equal(store["df"], df)

    # check that we have indices created
    assert store._handle.root.df.table.cols.index.is_indexed is True
    assert store._handle.root.df.table.cols.B.is_indexed is True

    # data column searching
    result = store.select("df", "B>0")
    expected = df[df.B > 0]
    tm.assert_frame_equal(result, expected)

    # data column searching (with an indexable and a data_columns)
    result = store.select("df", "B>0 and index>df.index[3]")
    df_new = df.reindex(index=df.index[4:])
    expected = df_new[df_new.B > 0]
    tm.assert_frame_equal(result, expected)

    # data column selection with a string data_column
    df_new = df.copy()
    df_new["string"] = "foo"
    df_new.loc[df_new.index[1:4], "string"] = np.nan
    df_new.loc[df_new.index[5:6], "string"] = "bar"
    _maybe_remove(store, "df")
    store.append("df", df_new, data_columns=["string"])
    result = store.select("df", "string='foo'")
    expected = df_new[df_new.string == "foo"]
    tm.assert_frame_equal(result, expected)

    # using min_itemsize and a data column
    def check_col(key, name, size):
        assert (
            getattr(store.get_storer(key).table.description, name).itemsize == size
        )

with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, "df")
    store.append("df", df_new, data_columns=["string"], min_itemsize={"string": 30})
    check_col("df", "string", 30)
    _maybe_remove(store, "df")
    store.append("df", df_new, data_columns=["string"], min_itemsize=30)
    check_col("df", "string", 30)
    _maybe_remove(store, "df")
    store.append("df", df_new, data_columns=["string"], min_itemsize={"values": 30})
    check_col("df", "string", 30)

with ensure_clean_store(setup_path) as store:
    df_new["string2"] = "foobarbah"
    df_new["string_block1"] = "foobarbah1"
    df_new["string_block2"] = "foobarbah2"
    _maybe_remove(store, "df")
    store.append(
        "df",
        df_new,
        data_columns=["string", "string2"],
        min_itemsize={"string": 30, "string2": 40, "values": 50},
    )
    check_col("df", "string", 30)
    check_col("df", "string2", 40)
    check_col("df", "values_block_1", 50)

with ensure_clean_store(setup_path) as store:
    # multiple data columns
    df_new = df.copy()
    df_new.iloc[0, df_new.columns.get_loc("A")] = 1.0
    df_new.iloc[0, df_new.columns.get_loc("B")] = -1.0
    df_new["string"] = "foo"

    sl = df_new.columns.get_loc("string")
    df_new.iloc[1:4, sl] = np.nan
    df_new.iloc[5:6, sl] = "bar"

    df_new["string2"] = "foo"
    sl = df_new.columns.get_loc("string2")
    df_new.iloc[2:5, sl] = np.nan
    df_new.iloc[7:8, sl] = "bar"
    _maybe_remove(store, "df")
    store.append("df", df_new, data_columns=["A", "B", "string", "string2"])
    result = store.select("df", "string='foo' and string2='foo' and A>0 and B<0")
    expected = df_new[
        (df_new.string == "foo")
        & (df_new.string2 == "foo")
        & (df_new.A > 0)
        & (df_new.B < 0)
    ]
    tm.assert_frame_equal(result, expected, check_freq=False)
    # FIXME: 2020-05-07 freq check randomly fails in the CI

    # yield an empty frame
    result = store.select("df", "string='foo' and string2='cool'")
    expected = df_new[(df_new.string == "foo") & (df_new.string2 == "cool")]
    tm.assert_frame_equal(result, expected)

with ensure_clean_store(setup_path) as store:
    # doc example
    df_dc = df.copy()
    df_dc["string"] = "foo"
    df_dc.loc[df_dc.index[4:6], "string"] = np.nan
    df_dc.loc[df_dc.index[7:9], "string"] = "bar"
    df_dc["string2"] = "cool"
    df_dc["datetime"] = Timestamp("20010102")
    df_dc.loc[df_dc.index[3:5], ["A", "B", "datetime"]] = np.nan

    _maybe_remove(store, "df_dc")
    store.append(
        "df_dc", df_dc, data_columns=["B", "C", "string", "string2", "datetime"]
    )
    result = store.select("df_dc", "B>0")

    expected = df_dc[df_dc.B > 0]
    tm.assert_frame_equal(result, expected)

    result = store.select("df_dc", ["B > 0", "C > 0", "string == foo"])
    expected = df_dc[(df_dc.B > 0) & (df_dc.C > 0) & (df_dc.string == "foo")]
    tm.assert_frame_equal(result, expected, check_freq=False)
    # FIXME: 2020-12-07 intermittent build failures here with freq of
    #  None instead of BDay(4)

with ensure_clean_store(setup_path) as store:
    # doc example part 2
    np.random.seed(1234)
    index = date_range("1/1/2000", periods=8)
    df_dc = DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
    df_dc["string"] = "foo"
    df_dc.loc[df_dc.index[4:6], "string"] = np.nan
    df_dc.loc[df_dc.index[7:9], "string"] = "bar"
    df_dc[["B", "C"]] = df_dc[["B", "C"]].abs()
    df_dc["string2"] = "cool"

    # on-disk operations
    store.append("df_dc", df_dc, data_columns=["B", "C", "string", "string2"])

    result = store.select("df_dc", "B>0")
    expected = df_dc[df_dc.B > 0]
    tm.assert_frame_equal(result, expected)

    result = store.select("df_dc", ["B > 0", "C > 0", 'string == "foo"'])
    expected = df_dc[(df_dc.B > 0) & (df_dc.C > 0) & (df_dc.string == "foo")]
    tm.assert_frame_equal(result, expected)
