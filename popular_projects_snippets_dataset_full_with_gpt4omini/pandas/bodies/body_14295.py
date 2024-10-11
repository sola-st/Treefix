# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

with ensure_clean_store(setup_path) as store:

    # test append with invalid input to get good error messages

    # list in column
    df = tm.makeDataFrame()
    df["invalid"] = [["a"]] * len(df)
    assert df.dtypes["invalid"] == np.object_
    msg = re.escape(
        """Cannot serialize the column [invalid]
because its data contents are not [string] but [mixed] object dtype"""
    )
    with pytest.raises(TypeError, match=msg):
        store.append("df", df)

    # multiple invalid columns
    df["invalid2"] = [["a"]] * len(df)
    df["invalid3"] = [["a"]] * len(df)
    with pytest.raises(TypeError, match=msg):
        store.append("df", df)

    # datetime with embedded nans as object
    df = tm.makeDataFrame()
    s = Series(datetime.datetime(2001, 1, 2), index=df.index)
    s = s.astype(object)
    s[0:5] = np.nan
    df["invalid"] = s
    assert df.dtypes["invalid"] == np.object_
    msg = "too many timezones in this block, create separate data columns"
    with pytest.raises(TypeError, match=msg):
        store.append("df", df)

    # directly ndarray
    msg = "value must be None, Series, or DataFrame"
    with pytest.raises(TypeError, match=msg):
        store.append("df", np.arange(10))

    # series directly
    msg = re.escape(
        "cannot properly create the storer for: "
        "[group->df,value-><class 'pandas.core.series.Series'>]"
    )
    with pytest.raises(TypeError, match=msg):
        store.append("df", Series(np.arange(10)))

    # appending an incompatible table
    df = tm.makeDataFrame()
    store.append("df", df)

    df["foo"] = "foo"
    msg = re.escape(
        "invalid combination of [non_index_axes] on appending data "
        "[(1, ['A', 'B', 'C', 'D', 'foo'])] vs current table "
        "[(1, ['A', 'B', 'C', 'D'])]"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df", df)

    # incompatible type (GH 41897)
    _maybe_remove(store, "df")
    df["foo"] = Timestamp("20130101")
    store.append("df", df)
    df["foo"] = "bar"
    msg = re.escape(
        "invalid combination of [values_axes] on appending data "
        "[name->values_block_1,cname->values_block_1,"
        "dtype->bytes24,kind->string,shape->(1, 30)] "
        "vs current table "
        "[name->values_block_1,cname->values_block_1,"
        "dtype->datetime64,kind->datetime64,shape->None]"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df", df)
