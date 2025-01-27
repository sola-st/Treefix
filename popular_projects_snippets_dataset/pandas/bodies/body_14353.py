# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:
    store["a"] = tm.makeTimeDataFrame()
    ts = tm.makeTimeSeries()
    store["a"] = ts

    tm.assert_series_equal(store["a"], ts)
