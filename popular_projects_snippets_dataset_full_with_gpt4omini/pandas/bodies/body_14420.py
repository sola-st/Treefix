# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_time_series.py

with ensure_clean_store(setup_path) as store:
    dt = datetime.datetime(2012, 1, 2, 3, 4, 5, 123456)
    series = Series([0], [dt])
    store["a"] = series
    assert store["a"].index[0] == dt
