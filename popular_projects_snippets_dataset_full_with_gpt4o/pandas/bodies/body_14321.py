# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# GH 20594

dtype = pd.DatetimeTZDtype(tz=tz_aware_fixture)

with ensure_clean_store(setup_path) as store:
    s = Series([0], dtype=dtype)
    store["s"] = s
    result = store["s"]
    tm.assert_series_equal(result, s)
