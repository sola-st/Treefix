# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py

df = tm.makeTimeDataFrame()

with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, "df")

    # GH 17912
    # HDFStore.select_column should raise a KeyError
    # exception if the key is not a valid store
    with pytest.raises(KeyError, match="No object named df in the file"):
        store.select_column("df", "index")

    store.append("df", df)
    # error
    with pytest.raises(
        KeyError, match=re.escape("'column [foo] not found in the table'")
    ):
        store.select_column("df", "foo")

    msg = re.escape("select_column() got an unexpected keyword argument 'where'")
    with pytest.raises(TypeError, match=msg):
        store.select_column("df", "index", where=["index>5"])

    # valid
    result = store.select_column("df", "index")
    tm.assert_almost_equal(result.values, Series(df.index).values)
    assert isinstance(result, Series)

    # not a data indexable column
    msg = re.escape(
        "column [values_block_0] can not be extracted individually; "
        "it is not data indexable"
    )
    with pytest.raises(ValueError, match=msg):
        store.select_column("df", "values_block_0")

    # a data column
    df2 = df.copy()
    df2["string"] = "foo"
    store.append("df2", df2, data_columns=["string"])
    result = store.select_column("df2", "string")
    tm.assert_almost_equal(result.values, df2["string"].values)

    # a data column with NaNs, result excludes the NaNs
    df3 = df.copy()
    df3["string"] = "foo"
    df3.loc[df3.index[4:6], "string"] = np.nan
    store.append("df3", df3, data_columns=["string"])
    result = store.select_column("df3", "string")
    tm.assert_almost_equal(result.values, df3["string"].values)

    # start/stop
    result = store.select_column("df3", "string", start=2)
    tm.assert_almost_equal(result.values, df3["string"].values[2:])

    result = store.select_column("df3", "string", start=-2)
    tm.assert_almost_equal(result.values, df3["string"].values[-2:])

    result = store.select_column("df3", "string", stop=2)
    tm.assert_almost_equal(result.values, df3["string"].values[:2])

    result = store.select_column("df3", "string", stop=-2)
    tm.assert_almost_equal(result.values, df3["string"].values[:-2])

    result = store.select_column("df3", "string", start=2, stop=-2)
    tm.assert_almost_equal(result.values, df3["string"].values[2:-2])

    result = store.select_column("df3", "string", start=-2, stop=2)
    tm.assert_almost_equal(result.values, df3["string"].values[-2:2])

    # GH 10392 - make sure column name is preserved
    df4 = DataFrame({"A": np.random.randn(10), "B": "foo"})
    store.append("df4", df4, data_columns=True)
    expected = df4["B"]
    result = store.select_column("df4", "B")
    tm.assert_series_equal(result, expected)
