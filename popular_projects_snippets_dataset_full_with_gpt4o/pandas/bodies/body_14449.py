# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py
# select via complex criteria

df = tm.makeTimeDataFrame()
df["string"] = "foo"
df.loc[df.index[0:4], "string"] = "bar"

with ensure_clean_store(setup_path) as store:
    store.put("df", df, format="table", data_columns=["string"])

    # empty
    result = store.select("df", 'index>df.index[3] & string="bar"')
    expected = df.loc[(df.index > df.index[3]) & (df.string == "bar")]
    tm.assert_frame_equal(result, expected)

    result = store.select("df", 'index>df.index[3] & string="foo"')
    expected = df.loc[(df.index > df.index[3]) & (df.string == "foo")]
    tm.assert_frame_equal(result, expected)

    # or
    result = store.select("df", 'index>df.index[3] | string="bar"')
    expected = df.loc[(df.index > df.index[3]) | (df.string == "bar")]
    tm.assert_frame_equal(result, expected)

    result = store.select(
        "df", '(index>df.index[3] & index<=df.index[6]) | string="bar"'
    )
    expected = df.loc[
        ((df.index > df.index[3]) & (df.index <= df.index[6]))
        | (df.string == "bar")
    ]
    tm.assert_frame_equal(result, expected)

    # invert
    result = store.select("df", 'string!="bar"')
    expected = df.loc[df.string != "bar"]
    tm.assert_frame_equal(result, expected)

    # invert not implemented in numexpr :(
    msg = "cannot use an invert condition when passing to numexpr"
    with pytest.raises(NotImplementedError, match=msg):
        store.select("df", '~(string="bar")')

    # invert ok for filters
    result = store.select("df", "~(columns=['A','B'])")
    expected = df.loc[:, df.columns.difference(["A", "B"])]
    tm.assert_frame_equal(result, expected)

    # in
    result = store.select("df", "index>df.index[3] & columns in ['A','B']")
    expected = df.loc[df.index > df.index[3]].reindex(columns=["A", "B"])
    tm.assert_frame_equal(result, expected)
