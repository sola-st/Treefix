# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# GH7777
# selecting a UTC datetimeindex column did
# not preserve UTC tzinfo set before storing

# check that no tz still works
rng = date_range("1/1/2000", "1/30/2000")
frame = DataFrame(np.random.randn(len(rng), 4), index=rng)

with ensure_clean_store(setup_path) as store:
    store.append("frame", frame)
    result = store.select_column("frame", "index")
    assert rng.tz == DatetimeIndex(result.values).tz

# check utc
rng = date_range("1/1/2000", "1/30/2000", tz="UTC")
frame = DataFrame(np.random.randn(len(rng), 4), index=rng)

with ensure_clean_store(setup_path) as store:
    store.append("frame", frame)
    result = store.select_column("frame", "index")
    assert rng.tz == result.dt.tz

# double check non-utc
rng = date_range("1/1/2000", "1/30/2000", tz="US/Eastern")
frame = DataFrame(np.random.randn(len(rng), 4), index=rng)

with ensure_clean_store(setup_path) as store:
    store.append("frame", frame)
    result = store.select_column("frame", "index")
    assert rng.tz == result.dt.tz
