# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
with ensure_clean_store(setup_path) as store:

    # index
    rng = date_range("1/1/2000", "1/30/2000", tz="US/Eastern")
    rng = rng._with_freq(None)  # freq doesn't round-trip
    df = DataFrame(np.random.randn(len(rng), 4), index=rng)
    store["df"] = df
    result = store["df"]
    tm.assert_frame_equal(result, df)

    # as data
    # GH11411
    _maybe_remove(store, "df")
    df = DataFrame(
        {
            "A": rng,
            "B": rng.tz_convert("UTC").tz_localize(None),
            "C": rng.tz_convert("CET"),
            "D": range(len(rng)),
        },
        index=rng,
    )
    store["df"] = df
    result = store["df"]
    tm.assert_frame_equal(result, df)
