# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# GH#4098 example

dti = date_range("2000-1-1", periods=3, freq="H", tz=gettz("US/Eastern"))
dti = dti._with_freq(None)  # freq doesn't round-trip

df = DataFrame({"A": Series(range(3), index=dti)})

with ensure_clean_store(setup_path) as store:

    _maybe_remove(store, "df")
    store.put("df", df)
    result = store.select("df")
    tm.assert_frame_equal(result, df)

    _maybe_remove(store, "df")
    store.append("df", df)
    result = store.select("df")
    tm.assert_frame_equal(result, df)
