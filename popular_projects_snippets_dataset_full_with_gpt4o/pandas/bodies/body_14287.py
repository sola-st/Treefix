# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

with ensure_clean_store(setup_path) as store:
    with catch_warnings(record=True):

        def check_col(key, name, size):
            assert (
                getattr(store.get_storer(key).table.description, name).itemsize
                == size
            )

        # avoid truncation on elements
        df = DataFrame([[123, "asdqwerty"], [345, "dggnhebbsdfbdfb"]])
        store.append("df_big", df)
        tm.assert_frame_equal(store.select("df_big"), df)
        check_col("df_big", "values_block_1", 15)

        # appending smaller string ok
        df2 = DataFrame([[124, "asdqy"], [346, "dggnhefbdfb"]])
        store.append("df_big", df2)
        expected = concat([df, df2])
        tm.assert_frame_equal(store.select("df_big"), expected)
        check_col("df_big", "values_block_1", 15)

        # avoid truncation on elements
        df = DataFrame([[123, "asdqwerty"], [345, "dggnhebbsdfbdfb"]])
        store.append("df_big2", df, min_itemsize={"values": 50})
        tm.assert_frame_equal(store.select("df_big2"), df)
        check_col("df_big2", "values_block_1", 50)

        # bigger string on next append
        store.append("df_new", df)
        df_new = DataFrame(
            [[124, "abcdefqhij"], [346, "abcdefghijklmnopqrtsuvwxyz"]]
        )
        msg = (
            r"Trying to store a string with len \[26\] in "
            r"\[values_block_1\] column but\n"
            r"this column has a limit of \[15\]!\n"
            "Consider using min_itemsize to preset the sizes on these "
            "columns"
        )
        with pytest.raises(ValueError, match=msg):
            store.append("df_new", df_new)

        # min_itemsize on Series index (GH 11412)
        df = tm.makeMixedDataFrame().set_index("C")
        store.append("ss", df["B"], min_itemsize={"index": 4})
        tm.assert_series_equal(store.select("ss"), df["B"])

        # same as above, with data_columns=True
        store.append("ss2", df["B"], data_columns=True, min_itemsize={"index": 4})
        tm.assert_series_equal(store.select("ss2"), df["B"])

        # min_itemsize in index without appending (GH 10381)
        store.put("ss3", df, format="table", min_itemsize={"index": 6})
        # just make sure there is a longer string:
        df2 = df.copy().reset_index().assign(C="longer").set_index("C")
        store.append("ss3", df2)
        tm.assert_frame_equal(store.select("ss3"), concat([df, df2]))

        # same as above, with a Series
        store.put("ss4", df["B"], format="table", min_itemsize={"index": 6})
        store.append("ss4", df2["B"])
        tm.assert_series_equal(store.select("ss4"), concat([df["B"], df2["B"]]))

        # with nans
        _maybe_remove(store, "df")
        df = tm.makeTimeDataFrame()
        df["string"] = "foo"
        df.loc[df.index[1:4], "string"] = np.nan
        df["string2"] = "bar"
        df.loc[df.index[4:8], "string2"] = np.nan
        df["string3"] = "bah"
        df.loc[df.index[1:], "string3"] = np.nan
        store.append("df", df)
        result = store.select("df")
        tm.assert_frame_equal(result, df)

with ensure_clean_store(setup_path) as store:

    df = DataFrame({"A": "foo", "B": "bar"}, index=range(10))

    # a min_itemsize that creates a data_column
    _maybe_remove(store, "df")
    store.append("df", df, min_itemsize={"A": 200})
    check_col("df", "A", 200)
    assert store.get_storer("df").data_columns == ["A"]

    # a min_itemsize that creates a data_column2
    _maybe_remove(store, "df")
    store.append("df", df, data_columns=["B"], min_itemsize={"A": 200})
    check_col("df", "A", 200)
    assert store.get_storer("df").data_columns == ["B", "A"]

    # a min_itemsize that creates a data_column2
    _maybe_remove(store, "df")
    store.append("df", df, data_columns=["B"], min_itemsize={"values": 200})
    check_col("df", "B", 200)
    check_col("df", "values_block_0", 200)
    assert store.get_storer("df").data_columns == ["B"]

    # infer the .typ on subsequent appends
    _maybe_remove(store, "df")
    store.append("df", df[:5], min_itemsize=200)
    store.append("df", df[5:], min_itemsize=200)
    tm.assert_frame_equal(store["df"], df)

    # invalid min_itemsize keys
    df = DataFrame(["foo", "foo", "foo", "barh", "barh", "barh"], columns=["A"])
    _maybe_remove(store, "df")
    msg = re.escape(
        "min_itemsize has the key [foo] which is not an axis or data_column"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df", df, min_itemsize={"foo": 20, "foobar": 20})
