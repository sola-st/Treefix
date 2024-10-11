# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

with ensure_clean_store(setup_path) as store:
    df = tm.makeDataFrame()
    store.append("df", df, chunksize=1)
    result = store.select("df")
    tm.assert_frame_equal(result, df)

    store.append("df1", df, expectedrows=10)
    result = store.select("df1")
    tm.assert_frame_equal(result, df)
