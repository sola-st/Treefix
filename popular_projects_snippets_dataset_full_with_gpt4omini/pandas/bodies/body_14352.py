# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
df = tm.makeDataFrame()
series = df["A"]

with ensure_clean_store(setup_path) as store:
    store["series"] = series
    recons = store["series"]
    tm.assert_series_equal(recons, series)
