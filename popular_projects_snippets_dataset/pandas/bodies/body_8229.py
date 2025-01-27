# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
# make sure we can make the round trip
freq = f"Q-{month}"
rng = period_range("1989Q3", "1991Q3", freq=freq)
stamps = rng.to_timestamp()
result = stamps.to_period(freq)
tm.assert_index_equal(rng, result)
