# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# GH 17618
time = Timestamp("2000-01-01 01:00:00", tz="US/Eastern")
df = DataFrame(data=[0], index=[time])

with ensure_clean_store(setup_path) as store:
    store.put("frame", df, format="fixed")
    recons = store["frame"]
    tm.assert_frame_equal(recons, df)
    assert recons.index[0].value == 946706400000000000
