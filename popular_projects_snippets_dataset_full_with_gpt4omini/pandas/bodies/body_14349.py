# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:

    df = DataFrame(np.random.randn(20, 2), index=date_range("20130101", periods=20))
    store.put("df", df, format="table")
    expected = df[df.index > Timestamp("20130105")]

    result = store.select("df", "index>datetime.datetime(2013,1,5)")
    tm.assert_frame_equal(result, expected)

    # changes what 'datetime' points to in the namespace where
    #  'select' does the lookup

    # technically an error, but allow it
    result = store.select("df", "index>datetime.datetime(2013,1,5)")
    tm.assert_frame_equal(result, expected)

    result = store.select("df", "index>datetime(2013,1,5)")
    tm.assert_frame_equal(result, expected)
