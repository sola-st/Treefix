# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

# single table
with ensure_clean_store(setup_path) as store:

    df = tm.makeTimeDataFrame(500)
    _maybe_remove(store, "df")
    store.append("df", df)

    expected = store.select("df")

    results = list(store.select("df", iterator=True))
    result = concat(results)
    tm.assert_frame_equal(expected, result)

    results = list(store.select("df", chunksize=100))
    assert len(results) == 5
    result = concat(results)
    tm.assert_frame_equal(expected, result)

    results = list(store.select("df", chunksize=150))
    result = concat(results)
    tm.assert_frame_equal(result, expected)

path = tmp_path / setup_path

df = tm.makeTimeDataFrame(500)
df.to_hdf(path, "df_non_table")

msg = "can only use an iterator or chunksize on a table"
with pytest.raises(TypeError, match=msg):
    read_hdf(path, "df_non_table", chunksize=100)

with pytest.raises(TypeError, match=msg):
    read_hdf(path, "df_non_table", iterator=True)

path = tmp_path / setup_path

df = tm.makeTimeDataFrame(500)
df.to_hdf(path, "df", format="table")

results = list(read_hdf(path, "df", chunksize=100))
result = concat(results)

assert len(results) == 5
tm.assert_frame_equal(result, df)
tm.assert_frame_equal(result, read_hdf(path, "df"))

# multiple

with ensure_clean_store(setup_path) as store:

    df1 = tm.makeTimeDataFrame(500)
    store.append("df1", df1, data_columns=True)
    df2 = tm.makeTimeDataFrame(500).rename(columns="{}_2".format)
    df2["foo"] = "bar"
    store.append("df2", df2)

    df = concat([df1, df2], axis=1)

    # full selection
    expected = store.select_as_multiple(["df1", "df2"], selector="df1")
    results = list(
        store.select_as_multiple(["df1", "df2"], selector="df1", chunksize=150)
    )
    result = concat(results)
    tm.assert_frame_equal(expected, result)
