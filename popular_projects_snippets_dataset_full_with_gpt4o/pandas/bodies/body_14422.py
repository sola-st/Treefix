# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_time_series.py

with ensure_clean_store(setup_path) as store:
    idx = tm.makeDateIndex(10)
    df = DataFrame(np.random.randn(len(idx), 3), index=idx)
    store["a"] = df
    result = store["a"]

    tm.assert_frame_equal(result, df)
    assert result.index.freq == df.index.freq
    tm.assert_class_equal(result.index, df.index, obj="dataframe index")

    idx = tm.makePeriodIndex(10)
    df = DataFrame(np.random.randn(len(idx), 3), idx)
    store["a"] = df
    result = store["a"]

    tm.assert_frame_equal(result, df)
    assert result.index.freq == df.index.freq
    tm.assert_class_equal(result.index, df.index, obj="dataframe index")
