# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
df = multiindex_dataframe_random_data
df.columns.name = None

with ensure_clean_store(setup_path) as store:
    store.append("mi", df)
    result = store.select("mi")
    tm.assert_frame_equal(result, df)

    # GH 3748
    result = store.select("mi", columns=["A", "B"])
    expected = df.reindex(columns=["A", "B"])
    tm.assert_frame_equal(result, expected)

path = tmp_path / "test.hdf"
df.to_hdf(path, "df", format="table")
result = read_hdf(path, "df", columns=["A", "B"])
expected = df.reindex(columns=["A", "B"])
tm.assert_frame_equal(result, expected)
