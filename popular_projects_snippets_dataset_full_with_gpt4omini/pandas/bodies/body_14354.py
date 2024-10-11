# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
df = tm.makeTimeDataFrame()

with ensure_clean_store(setup_path) as store:

    _maybe_remove(store, "df")
    store.append("df", df)

    # all
    c = store.select_as_coordinates("df")
    assert (c.values == np.arange(len(df.index))).all()

    # get coordinates back & test vs frame
    _maybe_remove(store, "df")

    df = DataFrame({"A": range(5), "B": range(5)})
    store.append("df", df)
    c = store.select_as_coordinates("df", ["index<3"])
    assert (c.values == np.arange(3)).all()
    result = store.select("df", where=c)
    expected = df.loc[0:2, :]
    tm.assert_frame_equal(result, expected)

    c = store.select_as_coordinates("df", ["index>=3", "index<=4"])
    assert (c.values == np.arange(2) + 3).all()
    result = store.select("df", where=c)
    expected = df.loc[3:4, :]
    tm.assert_frame_equal(result, expected)
    assert isinstance(c, Index)

    # multiple tables
    _maybe_remove(store, "df1")
    _maybe_remove(store, "df2")
    df1 = tm.makeTimeDataFrame()
    df2 = tm.makeTimeDataFrame().rename(columns="{}_2".format)
    store.append("df1", df1, data_columns=["A", "B"])
    store.append("df2", df2)

    c = store.select_as_coordinates("df1", ["A>0", "B>0"])
    df1_result = store.select("df1", c)
    df2_result = store.select("df2", c)
    result = concat([df1_result, df2_result], axis=1)

    expected = concat([df1, df2], axis=1)
    expected = expected[(expected.A > 0) & (expected.B > 0)]
    tm.assert_frame_equal(result, expected, check_freq=False)
    # FIXME: 2021-01-18 on some (mostly windows) builds we get freq=None
    #  but expect freq="18B"

# pass array/mask as the coordinates
with ensure_clean_store(setup_path) as store:

    df = DataFrame(
        np.random.randn(1000, 2), index=date_range("20000101", periods=1000)
    )
    store.append("df", df)
    c = store.select_column("df", "index")
    where = c[DatetimeIndex(c).month == 5].index
    expected = df.iloc[where]

    # locations
    result = store.select("df", where=where)
    tm.assert_frame_equal(result, expected)

    # boolean
    result = store.select("df", where=where)
    tm.assert_frame_equal(result, expected)

    # invalid
    msg = (
        "where must be passed as a string, PyTablesExpr, "
        "or list-like of PyTablesExpr"
    )
    with pytest.raises(TypeError, match=msg):
        store.select("df", where=np.arange(len(df), dtype="float64"))

    with pytest.raises(TypeError, match=msg):
        store.select("df", where=np.arange(len(df) + 1))

    with pytest.raises(TypeError, match=msg):
        store.select("df", where=np.arange(len(df)), start=5)

    with pytest.raises(TypeError, match=msg):
        store.select("df", where=np.arange(len(df)), start=5, stop=10)

    # selection with filter
    selection = date_range("20000101", periods=500)
    result = store.select("df", where="index in selection")
    expected = df[df.index.isin(selection)]
    tm.assert_frame_equal(result, expected)

    # list
    df = DataFrame(np.random.randn(10, 2))
    store.append("df2", df)
    result = store.select("df2", where=[0, 3, 5])
    expected = df.iloc[[0, 3, 5]]
    tm.assert_frame_equal(result, expected)

    # boolean
    where = [True] * 10
    where[-2] = False
    result = store.select("df2", where=where)
    expected = df.loc[where]
    tm.assert_frame_equal(result, expected)

    # start/stop
    result = store.select("df2", start=5, stop=10)
    expected = df[5:10]
    tm.assert_frame_equal(result, expected)
