# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
# GH#2891
prng = period_range("1/1/2011", "1/1/2012", freq="M")
ts = Series(np.random.randn(len(prng)), prng)
new_ts = tm.round_trip_pickle(ts)
assert new_ts.index.freq == "M"
