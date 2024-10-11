# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

# monotonic
idx1 = TimedeltaIndex(["1 days", "2 days", "3 days"])
assert idx1.is_monotonic_increasing

# non-monotonic
idx2 = TimedeltaIndex(["1 days", np.nan, "3 days", "NaT"])
assert not idx2.is_monotonic_increasing

for idx in [idx1, idx2]:
    assert idx.min() == Timedelta("1 days")
    assert idx.max() == Timedelta("3 days")
    assert idx.argmin() == 0
    assert idx.argmax() == 2
