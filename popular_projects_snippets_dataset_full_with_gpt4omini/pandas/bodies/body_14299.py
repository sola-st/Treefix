# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
df1 = tm.makeTimeDataFrame()
df2 = tm.makeTimeDataFrame().rename(columns="{}_2".format)
df1.iloc[1, df1.columns.get_indexer(["A", "B"])] = np.nan
df = concat([df1, df2], axis=1)

with ensure_clean_store(setup_path) as store, pd.option_context(
    "io.hdf.dropna_table", True
):
    # dropna=False shouldn't synchronize row indexes
    store.append_to_multiple(
        {"df1a": ["A", "B"], "df2a": None}, df, selector="df1a", dropna=False
    )

    msg = "all tables must have exactly the same nrows!"
    with pytest.raises(ValueError, match=msg):
        store.select_as_multiple(["df1a", "df2a"])

    assert not store.select("df1a").index.equals(store.select("df2a").index)
