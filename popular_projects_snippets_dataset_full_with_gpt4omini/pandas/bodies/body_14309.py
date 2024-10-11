# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py

with ensure_clean_store(setup_path) as store:
    df = DataFrame({"A": "foo", "B": "bar"}, index=range(5))
    df.loc[2, "A"] = np.nan
    df.loc[3, "B"] = np.nan
    _maybe_remove(store, "df")
    store.append("df", df, encoding="ascii")
    tm.assert_frame_equal(store["df"], df)

    expected = df.reindex(columns=["A"])
    result = store.select("df", Term("columns=A", encoding="ascii"))
    tm.assert_frame_equal(result, expected)
