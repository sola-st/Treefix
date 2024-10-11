# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py

with tm.ensure_clean(setup_path) as path:

    df = tm.makeDataFrame()

    # create an in memory store
    store = HDFStore(
        path, mode="a", driver="H5FD_CORE", driver_core_backing_store=0
    )
    store["df"] = df
    store.append("df2", df)

    tm.assert_frame_equal(store["df"], df)
    tm.assert_frame_equal(store["df2"], df)

    store.close()

# the file should not have actually been written
assert not os.path.exists(path)
