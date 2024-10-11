# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

with ensure_clean_store(setup_path) as store:
    df1 = DataFrame({"a": [1, 2, 3]}, dtype="f8")
    store.append("df_f8", df1)
    tm.assert_series_equal(df1.dtypes, store["df_f8"].dtypes)

    df2 = DataFrame({"a": [1, 2, 3]}, dtype="i8")
    store.append("df_i8", df2)
    tm.assert_series_equal(df2.dtypes, store["df_i8"].dtypes)

    # incompatible dtype
    msg = re.escape(
        "invalid combination of [values_axes] on appending data "
        "[name->values_block_0,cname->values_block_0,"
        "dtype->float64,kind->float,shape->(1, 3)] vs "
        "current table [name->values_block_0,"
        "cname->values_block_0,dtype->int64,kind->integer,"
        "shape->None]"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df_i8", df1)

    # check creation/storage/retrieval of float32 (a bit hacky to
    # actually create them thought)
    df1 = DataFrame(np.array([[1], [2], [3]], dtype="f4"), columns=["A"])
    store.append("df_f4", df1)
    tm.assert_series_equal(df1.dtypes, store["df_f4"].dtypes)
    assert df1.dtypes[0] == "float32"

    # check with mixed dtypes
    df1 = DataFrame(
        {
            c: Series(np.random.randint(5), dtype=c)
            for c in ["float32", "float64", "int32", "int64", "int16", "int8"]
        }
    )
    df1["string"] = "foo"
    df1["float322"] = 1.0
    df1["float322"] = df1["float322"].astype("float32")
    df1["bool"] = df1["float32"] > 0
    df1["time1"] = Timestamp("20130101")
    df1["time2"] = Timestamp("20130102")

    store.append("df_mixed_dtypes1", df1)
    result = store.select("df_mixed_dtypes1").dtypes.value_counts()
    result.index = [str(i) for i in result.index]
    expected = Series(
        {
            "float32": 2,
            "float64": 1,
            "int32": 1,
            "bool": 1,
            "int16": 1,
            "int8": 1,
            "int64": 1,
            "object": 1,
            "datetime64[ns]": 2,
        }
    )
    result = result.sort_index()
    expected = expected.sort_index()
    tm.assert_series_equal(result, expected)
