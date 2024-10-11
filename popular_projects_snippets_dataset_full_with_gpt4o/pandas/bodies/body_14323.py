# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# GH2852
# issue storing datetime.date with a timezone as it resets when read
# back in a new timezone

# original method
with ensure_clean_store(setup_path) as store:

    today = date(2013, 9, 10)
    df = DataFrame([1, 2, 3], index=[today, today, today])
    store["obj1"] = df
    result = store["obj1"]
    tm.assert_frame_equal(result, df)

# with tz setting
with ensure_clean_store(setup_path) as store:

    with tm.set_timezone("EST5EDT"):
        today = date(2013, 9, 10)
        df = DataFrame([1, 2, 3], index=[today, today, today])
        store["obj1"] = df

    with tm.set_timezone("CST6CDT"):
        result = store["obj1"]

    tm.assert_frame_equal(result, df)
