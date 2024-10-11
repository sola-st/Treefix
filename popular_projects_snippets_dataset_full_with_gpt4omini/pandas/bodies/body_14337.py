# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:

    s = tm.makeTimeSeries()
    store["a"] = s

    # test attribute access
    result = store.a
    tm.assert_series_equal(result, s)
    result = getattr(store, "a")
    tm.assert_series_equal(result, s)

    df = tm.makeTimeDataFrame()
    store["df"] = df
    result = store.df
    tm.assert_frame_equal(result, df)

    # errors
    for x in ["d", "mode", "path", "handle", "complib"]:
        msg = f"'HDFStore' object has no attribute '{x}'"
        with pytest.raises(AttributeError, match=msg):
            getattr(store, x)

        # not stores
    for x in ["mode", "path", "handle", "complib"]:
        getattr(store, f"_{x}")
