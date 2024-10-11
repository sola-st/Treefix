# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_time_series.py

with ensure_clean_store(setup_path) as store:
    idx = tm.makeDateIndex(10)
    ser = Series(np.random.randn(len(idx)), idx)
    store["a"] = ser
    result = store["a"]

    tm.assert_series_equal(result, ser)
    assert result.index.freq == ser.index.freq
    tm.assert_class_equal(result.index, ser.index, obj="series index")

    idx = tm.makePeriodIndex(10)
    ser = Series(np.random.randn(len(idx)), idx)
    store["a"] = ser
    result = store["a"]

    tm.assert_series_equal(result, ser)
    assert result.index.freq == ser.index.freq
    tm.assert_class_equal(result.index, ser.index, obj="series index")
