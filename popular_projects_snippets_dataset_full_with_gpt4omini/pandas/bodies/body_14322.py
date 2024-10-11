# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
rng = date_range("1/1/2000 00:00:00-07:00", "1/30/2000 00:00:00-07:00")
frame = DataFrame(np.random.randn(len(rng), 4), index=rng)

with ensure_clean_store(setup_path) as store:
    store["frame"] = frame
    recons = store["frame"]
    tm.assert_index_equal(recons.index, rng)
    assert rng.tz == recons.index.tz
