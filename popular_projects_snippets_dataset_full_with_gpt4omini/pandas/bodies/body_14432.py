# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py
df = tm.makeTimeDataFrame()

with ensure_clean_store(setup_path) as store:

    # can't compress if format='fixed'
    msg = "Compression not supported on Fixed format stores"
    with pytest.raises(ValueError, match=msg):
        store.put("b", df, format="fixed", complib="blosc")

    store.put("c", df, format="table", complib="blosc")
    tm.assert_frame_equal(store["c"], df)
