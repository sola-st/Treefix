# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_pickle.py
# GH#2891
prng = period_range("1/1/2011", "1/1/2012", freq="M")
new_prng = tm.round_trip_pickle(prng)
assert new_prng.freq == offsets.MonthEnd()
assert new_prng.freqstr == "M"
