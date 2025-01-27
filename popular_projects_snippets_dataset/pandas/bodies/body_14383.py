# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
path = tmp_path / setup_path

df = tm.makeDataFrame()
df.to_hdf(path, "df", append=False, format="fixed")
tm.assert_frame_equal(read_hdf(path, "df"), df)

df.to_hdf(path, "df", append=False, format="f")
tm.assert_frame_equal(read_hdf(path, "df"), df)

df.to_hdf(path, "df", append=False)
tm.assert_frame_equal(read_hdf(path, "df"), df)

df.to_hdf(path, "df")
tm.assert_frame_equal(read_hdf(path, "df"), df)

with ensure_clean_store(setup_path) as store:

    df = tm.makeDataFrame()

    _maybe_remove(store, "df")
    store.append("df", df.iloc[:10], append=True, format="table")
    store.append("df", df.iloc[10:], append=True, format="table")
    tm.assert_frame_equal(store.select("df"), df)

    # append to False
    _maybe_remove(store, "df")
    store.append("df", df.iloc[:10], append=False, format="table")
    store.append("df", df.iloc[10:], append=True, format="table")
    tm.assert_frame_equal(store.select("df"), df)

    # formats
    _maybe_remove(store, "df")
    store.append("df", df.iloc[:10], append=False, format="table")
    store.append("df", df.iloc[10:], append=True, format="table")
    tm.assert_frame_equal(store.select("df"), df)

    _maybe_remove(store, "df")
    store.append("df", df.iloc[:10], append=False, format="table")
    store.append("df", df.iloc[10:], append=True, format=None)
    tm.assert_frame_equal(store.select("df"), df)
