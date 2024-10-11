# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# make sure we are not failing on transitions
with ensure_clean_store(setup_path) as store:
    times = date_range(
        "2013-10-26 23:00",
        "2013-10-27 01:00",
        tz="Europe/London",
        freq="H",
        ambiguous="infer",
    )
    times = times._with_freq(None)  # freq doesn't round-trip

    for i in [times, times + pd.Timedelta("10min")]:
        _maybe_remove(store, "df")
        df = DataFrame({"A": range(len(i)), "B": i}, index=i)
        store.append("df", df)
        result = store.select("df")
        tm.assert_frame_equal(result, df)
